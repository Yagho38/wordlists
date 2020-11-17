import requests

url = 'https://solyd.com.br'
cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

resposta = requests.get(url, headers=cabecalho)

print(resposta.text)
