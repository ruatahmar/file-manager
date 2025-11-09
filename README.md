An automated python file manager i made because my downloads folder is constantly unorganised

Features:
* Real-time folder monitoring
* Automatic sorting by file type
* Handles duplicate filenames safely (adds numerical suffixes)
* Simple configuration — just edit your folder paths
* Cross-compatible on Windows, macOS, and Linux

Tech Stack:
Language: Python
Libraries: watchdog, os, shutil, time, logging

How to Run
1. Clone this repository
  ```bash
  git clone https://github.com/ruatahmar/file-manager.git
  cd file-manager
  ```
2. Install dependencies
  ```bash
  pip install watchdog
  ```
3. Edit the directory paths at the top of the script to match your system.
4. Run the program
  ```bash
  python main.py
  ```
