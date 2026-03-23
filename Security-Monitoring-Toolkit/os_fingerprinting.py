## This tool identifies the system's operating system name and version. 
## It uses the `platform` library to retrieve this information and displays it on the screen.
def os_fingerprinting():
    import platform

    os_name = platform.system()
    os_version = platform.version()
    print(f"OS Name: {os_name}")
    print(f"OS Version: {os_version}")
