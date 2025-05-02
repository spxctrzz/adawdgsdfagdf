Dim args, shell, argument, batCommand
Set args = WScript.Arguments
If args.Count = 0 Then
    WScript.Echo "Usage: run_volume.vbs <argument>"
    WScript.Quit 1
End If

argument = args(0)
Set shell = CreateObject("WScript.Shell")

' Build command to run the batch file with the argument
batCommand = "cmd.exe /c volume.bat """ & argument & """"

' Run the command silently (0 = hidden window, False = don't wait)
shell.Run batCommand, 0, False