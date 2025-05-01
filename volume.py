import os
import sys
if len(sys.argv) > 1:
        arg = sys.argv[1]
        while True:
            os.system("nircmd.exe mutesysvolume 0")
            os.system(f"nircmd.exe changesysvolume {arg}")
