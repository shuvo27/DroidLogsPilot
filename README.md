# 📱DroidLogsPilot (CLI Tool)
DroidLogPilot – A powerful ADB-based tool for real-time monitoring and analysis of Android mobile app logs. Designed for developers, testers, and QA engineers to debug, trace issues, and ensure app performance with ease.

## ✨ Features

- ✅ View real-time logs from a connected Android device
- 🎯 Filter logs by app package name (tag)
- 🔍 Optionally search and select from installed apps
- 📁 Export logs to a file
- 🧪 Filter logs by log level (e.g., Error logs only)
- 💻 Easy-to-use CLI

---

## 📦 Prerequisites

- Python 3.6+
- Android Debug Bridge (ADB) must be installed and added to your system's PATH.

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

## 🚀 Getting Started
1. Clone the repository or copy the script.
2. Connect your Android device via USB and enable USB debugging.
3. Run the script:
   ```bash
   python DroidLogsPilot.py

## 📌 Notes
- This script uses adb logcat, so only logs available at runtime will be shown.
- Ensure your device is authorized and ADB is working (adb devices should list it).
## 📜 License
### MIT License

**Copyright © 2025 [shuvokarmakar277@gmail.com](mailto:shuvokarmakar277@gmail.com)**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software  
and associated documentation files (the “Software”), to deal in the Software without restriction,  
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,  
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,  
subject to the following conditions:

> The above copyright notice and this permission notice  
> shall be included in all copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,**  
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE  
AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## 👨‍💻 Author

**Shuvo Karmakar**  
🎯 Software Quality Assurance (SQA) Engineer at **GotiPath**  
🌐 Dhaka, Bangladesh  
📧 Email: [shuvokarmakar277@gmail.com](mailto:shuvokarmakar277@gmail.com)  

Feel free to reach out for collaboration, feedback, or questions!

---

