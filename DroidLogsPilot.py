import subprocess
import sys

# === Utility Functions ===

def run_adb_logcat(filter_tag=None, filter_level=None, export_to_file=False, filename="adb_logs.txt"):
    """
    Runs the adb logcat command with optional tag and level filters.
    If export_to_file is True, saves logs to a file.
    """
    try:
        # Construct the adb command
        command = ["adb", "logcat"]
        if filter_tag:
            command.append(f"{filter_tag}:V")  # Filter logs by tag
        if filter_level:
            command.append(f"*:{filter_level}")  # Filter logs by log level (e.g., E = Error)

        # Start adb logcat process and capture stdout
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        print("Streaming logs from the connected device. Press Ctrl+C to stop.\n")

        # Stream and optionally save logs
        if export_to_file:
            with open(filename, "w", encoding="utf-8") as file:
                for line in iter(process.stdout.readline, ""):
                    highlighted_line = highlight_errors(line)
                    sys.stdout.write(highlighted_line)
                    file.write(line)  # Save original log line to file
            print(f"\nLogs have been saved to {filename}.")
        else:
            for line in iter(process.stdout.readline, ""):
                sys.stdout.write(highlight_errors(line))

    except KeyboardInterrupt:
        print("\nStopping logcat...")  # User interrupted with Ctrl+C
    except FileNotFoundError:
        print("Error: adb not found. Please ensure it's installed and in your PATH.")
    finally:
        # Clean up: ensure the subprocess is terminated
        if 'process' in locals():
            process.terminate()


def highlight_errors(line):
    """
    Highlights error-related keywords in red for better visibility in terminal output.
    """
    return line.replace("error", "\033[91merror\033[0m") \
               .replace("Error", "\033[91mError\033[0m") \
               .replace("ERROR", "\033[91mERROR\033[0m")


def check_device_connection():
    """
    Checks if an Android device is connected via ADB.
    """
    try:
        result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        lines = result.stdout.strip().splitlines()

        # A connected device appears on the second line or later with "device" status
        if len(lines) > 1 and any("device" in line for line in lines[1:]):
            print("Device connected successfully.")
            return True
        print("No devices detected. Ensure USB debugging is enabled and the device is connected.")
    except FileNotFoundError:
        print("Error: adb not found. Please ensure it's installed and in your PATH.")
    return False


def list_installed_apps():
    """
    Returns a list of all installed app package names on the connected device.
    """
    try:
        result = subprocess.run(
            ["adb", "shell", "pm", "list", "packages"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Clean output lines to just package names
        return [line.replace("package:", "").strip() for line in result.stdout.splitlines()]
    except FileNotFoundError:
        print("Error: adb not found. Please ensure it's installed and in your PATH.")
        return []


def search_apps(apps, term):
    """
    Filters the app list based on a case-insensitive search term.
    """
    return [app for app in apps if term.lower() in app.lower()]


def get_user_choice(prompt, options):
    """
    Displays a list of options and returns the index (1-based) of the chosen option.
    Returns None for invalid inputs.
    """
    print(prompt)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    try:
        choice = int(input("Enter your choice: ").strip())
        if 1 <= choice <= len(options):
            return choice
    except ValueError:
        pass
    print("Invalid choice. Proceeding with default.")
    return None


# === Main Program ===

if __name__ == "__main__":
    # Default values
    filter_tag = None
    filter_level = None
    export_to_file = False
    filename = "adb_logs.txt"

    # Check for a connected Android device
    if not check_device_connection():
        print("Exiting script.")
        sys.exit()

    # Ask user if they want to filter logs by app
    choice = get_user_choice("\nWould you like to filter logs for a specific app?", ["Yes (Filter by app)", "No (Show all logs)"])

    if choice == 1:
        apps = list_installed_apps()
        if not apps:
            print("No apps found.")
        else:
            # Optionally search for an app name
            search_choice = get_user_choice("\nWould you like to search for an app?", ["Yes", "No(Show all apps)"])
            if search_choice == 1:
                term = input("Enter app package name: ").strip()
                apps = search_apps(apps, term)
                if not apps:
                    print("No apps found matching the search term.")

            # Display list of apps to choose from
            print("\nAvailable apps:")
            for idx, app in enumerate(apps, 1):
                print(f"{idx}. {app}")

            # Let user select an app for filtering
            try:
                app_choice = int(input("\nEnter the number of the app to filter logs for: ").strip())
                if 1 <= app_choice <= len(apps):
                    filter_tag = apps[app_choice - 1]
                else:
                    print("Invalid selection. Showing all logs.")
            except ValueError:
                print("Invalid input. Showing all logs.")

        # Ask if user wants to filter by log level
        level_choice = get_user_choice("\nWould you like to filter by log level?", ["Yes (Error logs only)", "No(All logs)"])
        if level_choice == 1:
            filter_level = "E"  # Only show Error level logs

        # Ask if user wants to export logs
        export_choice = get_user_choice("\nWould you like to export the logs to a file?", ["Yes", "No"])
        if export_choice == 1:
            export_to_file = True
            user_filename = input("Enter filename (default is 'adb_logs.txt'): ").strip()
            if user_filename:
                filename = user_filename

    # Run the logcat process with selected options
    run_adb_logcat(filter_tag, filter_level, export_to_file, filename)
