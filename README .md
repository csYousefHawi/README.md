# Security Monitoring Toolkit Documentation

## Project Overview
The Security Monitoring Toolkit is designed to perform multiple system and security analysis tasks to monitor and detect suspicious activity in a system. The toolkit includes several tasks such as OS fingerprinting, file scanning, process detection, network monitoring, and login activity analysis.

## Purpose

The toolkit `aims` to help users:

- Gain insights into their system’s operations and security status.
- Detect suspicious processes running as admin/root.
- Monitor network activity and identify listening ports.
- Analyze login activity and detect repeated failed attempts from specific IPs.
- Understand how different components of system security can be monitored programmatically.

## Features
- Multiple Analysis Tasks: Provides 5 separate tasks that cover OS fingerprinting, file scanning, process detection, network monitoring, and login analysis.
- Dual Interfaces: Includes both a Command-Line Menu and a Graphical User Interface (GUI) for flexible usage.
- Real-Time Monitoring: Tasks such as process detection and network monitoring provide live insights into the system.
- Easy to Extend: Each task is implemented as a self-contained function, making it simple to add or modify features.
- Educational Value: Shows how Python libraries (psutil, platform, os, re) can be used for security monitoring.

## Requirements
- Python 3.x
- `psutil` (library for process and network monitoring)
- `platform` (library for OS detection) 
- `os` and `re` (libraries for file scanning and log analysis)
- `tkinter` (for GUI version)

### How to Use

### Command-Line Version:
1. Clone the repository:
   ```bash
   git clone https://github.com/username/Security-Monitoring-Toolkit.git
   , Or, if you dont have `Git` on your computer, you can `download the zip file`.
   then ..
   
   cd Security-Monitoring-Toolkit
   ```
2. Open a terminal and run the following command to start the program:
    ```bash
    python Command-Line_Menu_Version.py
    ```
### GUI Version: 
   ```bash
    python GUI.py
   ```
## Notes
- The toolkit is modular: each task is implemented in a separate file and can be imported individually.
- The login.log file is generated automatically for testing the login activity analyzer if it does not exist.
- The toolkit is intended for educational purposes and can serve as a foundation for more advanced security projects.
- Designed to work cross-platform (Windows, Linux, macOS).
