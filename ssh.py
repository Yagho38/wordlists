import paramiko

host = '192.168.1.33'
user = 'hack'
passwd = 'hacked'


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)
while True:
	comando = input('command: ')
	entrada, saida, erros = client.exec_command(comando)
	print(saida.readlines())
