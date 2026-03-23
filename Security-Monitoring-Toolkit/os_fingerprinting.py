def os_fingerprinting():
    import platform

    os_name = platform.system()
    os_version = platform.version()
    print(f"OS Name: {os_name}")
    print(f"OS Version: {os_version}")