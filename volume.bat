@echo off
:loop
nircmd.exe mutesysvolume 0
nircmd.exe changesysvolume %1
goto loop
