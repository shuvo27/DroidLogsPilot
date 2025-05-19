### 🛠 Install ADB & Set Up ADB (if not already installed):

- **Windows:** [Download SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools)
   - **Extract:**  
       Right-click the ZIP file → **Extract All…** → Choose a destination folder (e.g., `C:\platform-tools`).
  - **Add to PATH:**
     - Press `Win + S`, type `Environment Variables`, and select **Edit the system environment variables**.
     - Click **Environment Variables...** at the bottom.
     - Under **System variables**, find and select the `Path` variable, then click **Edit**.
     - Click **New** and add the path to the extracted folder, e.g.,  
       `C:\platform-tools`
     - Click **OK** to close all dialogs.
  - **Verify installation:**
      - Open **Command Prompt** and run:  
       ```bash
       adb version
  
- **Linux:**
     - **Download:** [platform-tools-latest-linux.zip](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)
     - **Extract:**  
          Open Terminal and run (assuming download in ~/Downloads):
          ```bash
          unzip ~/Downloads/platform-tools-latest-linux.zip -d ~/platform-tools
     - **Add to PATH:**
          Append the following line to your shell configuration file (depending on your shell):
          - For bash (~/.bashrc or ~/.bash_profile):
         ```bash
         export PATH="$HOME/platform-tools:$PATH"
         ```
          - For zsh (~/.zshrc):
        ```bash
        export PATH="$HOME/platform-tools:$PATH"
        ```
        Then reload the config:
       ```bash
       source ~/.bashrc   # or source ~/.zshrc depending on your shell
       ```
    - **Verify installation:**
        Run:
        ```bash
        adb version
        ```
       You should see ADB version info.
- **macOS:**
     - **Download:** [platform-tools-latest-darwin.zip](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip)
     - **Extract:**  
          Open Terminal and run (assuming download in ~/Downloads):
          ```bash
          unzip ~/Downloads/platform-tools-latest-darwin.zip -d ~/platform-tools
     - **Add to PATH:**
          Append the following line to your shell configuration file (depending on your shell):
          - For bash (~/.bashrc or ~/.bash_profile):
         ```bash
         export PATH="$HOME/platform-tools:$PATH"
         ```
        Then reload the config:
       ```bash
       source ~/.zshrc   # or source ~/.bash_profile
       ```
    - **Verify installation:**
        Run:
        ```bash
        adb version
        ```

- **Additional Tips**
  - **Grant executable permission on Linux/macOS:**
      Sometimes you may need to set executable permission:
      ```bash
      chmod +x ~/platform-tools/adb
      ```
  - **Check device connectivity:**
      Connect your Android device via USB (with Developer Options and USB Debugging enabled) and run:
      ```bash
      adb devices
      ```
  - **Update ADB:**
      Re-download the latest platform-tools from the official site to update.

- **ADB Installation Tutorial:** [Installation Tutorial](https://video.adsninja.ca/valnetinc/XDA/65f341f3e8c38-projectRssVideoFile.mp4)
