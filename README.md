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
- **macOS/Linux:**  
  ```bash
  brew install android-platform-tools  # macOS
  sudo apt install android-tools-adb   # Ubuntu/Debian
  ```
- Detailed steps for ADB installation and configuration can be found in the [ADB Installation](adbInstallation.md) documentation.
  
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
The MIT License (MIT). See the [LICENSE](LICENSE.md) file for complete information.

## 👨‍💻 Author

**Shuvo Karmakar**  
🎯 Software Quality Assurance (SQA) Engineer at **GotiPath**  
🌐 Dhaka, Bangladesh  
📧 Email: [shuvokarmakar277@gmail.com](mailto:shuvokarmakar277@gmail.com)  

Feel free to reach out for collaboration, feedback, or questions!

---

