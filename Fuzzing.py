import requests
import sys

arquivo = open(sys.argv[2])

url = sys.argv[1]

urls = arquivo.readlines()

for i in urls:

	cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

	resposta = requests.get((url + i), headers=cabecalho)

	if resposta.status_code != 404 and i[0] != "#":
		print(str(url) + str(i) + str(resposta.status_code))
