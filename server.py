import socket



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 4444

try:
	server.bind((ip, port))
	server.listen(5)
	print("Listening in: " + ip + ": " + str(port))
	client_socket, address = server.accept()
	print("received from: " + address[0])
	while True:
		data = client_socket.recv(1024)
		print("\n" + data)
		voce = raw_input("\nvoce: ")
		client_socket.send(voce)
	server.close()

except Exception as erro:

	print("Conexao falhou")

	print(erro)
	
	server.close()
