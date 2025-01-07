
' scriptDir = Left(WScript.ScriptFullName, InStrRev(WScript.ScriptFullName, "\") - 1)
' WScript.Echo( scriptDir )
Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("marvel.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("wonka.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("wish.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("tgr.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("sam.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("nepo.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("jig.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("japan.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("fail.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("era.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("dunki.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("animal.txt",2,true)
objFileToWrite.WriteLine(400)
objFileToWrite.Close
Set objFileToWrite = Nothing

WScript.Echo( "Bingo!!! Update completed" )
