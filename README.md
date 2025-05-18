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

