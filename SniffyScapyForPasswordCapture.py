import socket
import struct
from scapy.all import *

def imprime_pacote(pacote):
	header = str(pacote[TCP].payload)[0:4]
	if header == 'POST':
		print(pacote[0].show())


pacote = sniff(filter='port 80', store=0, prn=imprime_pacote)

#wrpcap("pacote.pcap", pacote)

#print(pacote[0].show())
