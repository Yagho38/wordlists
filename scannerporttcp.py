import socket


ip = str(input("Digite o ip: "))
ports = range(65535)


for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.15)
	code = client.connect_ex((ip, port))
	if code == 0:
		print("Porta " + str(port) + " aberta")



