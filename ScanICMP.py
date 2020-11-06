import random
import socket
import time
import ipaddress
from threading import Thread
import struct

SIGNAL = True

def checksum(source_string):
	sum = 0
	count_to = (len(source_string) / 2) * 2
	count = 0
	while count < count_to:
		this_val = ord(source_string[count + 1]) * 256 + ord(source_string[count])
		sum = sum + this_val
		sum = sum & 0xffffffff
		count = count + 2
	if count_to < len(source_string):
		sum = sum + ord(source_string[len(source_string) - 1])
		sum = sum & 0xffffffff
	sum = (sum >> 16) + (sum & 0xffff)
	sum = sum + (sum >> 16)
	answer = ~sum
	answer = answer & 0xffff

def create_packet(id):
	header = struct.pack('bbHHh', 8, 0, 0, id, 1)
	data = 192 * 'Q'
	my_checksum = checksum(header + data)
	header = struct.pack('bbHHh', 8, 0, socket.htons(my_checksum), id, 1)
	return header + data

def ping(addr, timeout=1):
	try:
		my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
	except Exception as e:
		print(e)
	packet_id = int((id(timeout) * random.random()) % 65535)
	packet = create_packet(packet_id)
	my_socket.connect((addr, 80))
	my_socket.sendall(packet)
	my_socket.close()
	return

def rotate()