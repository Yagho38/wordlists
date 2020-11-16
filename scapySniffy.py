from scapy.all import *

pacote = IP(version=4, dst=["google.com", "facebook.com"])/TCP(dport=[80, 443, 8080], flags='S')

recebido, naorecebido = sr(pacote, timeout=1)

if len(recebido) > 0:
	for i in range(len(recebido)):
		print(recebido[i][0][IP].dst, ":", pacote[i][0][TCP].dport)

