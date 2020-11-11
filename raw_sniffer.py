import socket
import struct

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
#s.bind(('eth0', 0))
count = 0

while True:
	packet = s.recvfrom(65565)
	traduzido = struct.unpack('!BBHHHBBH4s4s', packet[0][0:20])
	print('From: ', packet[1][0])
	print('Pacote: ', count, traduzido)
#	print('IPV', (traduzido[0] >> 4))
#	print('IP Header Length: ', (traduzido[0] << 4))
#	print('TTL: ', (traduzido[5]))
#	print('Protocol: ', (traduzido[6]))
#	print('Source IP: ', socket.inet_ntoa(traduzido[8]))
#	print('Target IP: ', socket.inet_ntoa(traduzido[9]))
	print('Conteudo: ', packet[0])
	count += 1
