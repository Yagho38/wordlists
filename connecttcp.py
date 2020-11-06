import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
porta = 1350
try:
	while True:
	       client.sendto(raw_input("Voce: "), (ip, porta))
	       msg, friend = client.recvfrom(1024)
	       print(friend[0] + ": " + msg)
	client.close()
except Exception as erro:
	print("Conexao falhou")
	print(erro)
	client.close()
