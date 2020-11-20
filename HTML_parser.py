from bs4 import BeautifulSoup
import requests

i = 1
url = 'https://g1.globo.com'
cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
req = requests.get(url, headers=cabecalho)
html = req.text

soup = BeautifulSoup(html, 'html.parser')

pegado = soup.find_all(class_="feed-post-link gui-color-primary gui-color-hover")  #soup.prettify()


url = 'https://br.investing.com/currencies/usd-brl'

req = requests.get(url, headers=cabecalho)

html = req.text

soup = BeautifulSoup(html, 'html.parser')

dolar = soup.find(id="last_last")

for item in pegado:
	print(i, "º ", item.get_text())
	i += 1
	
print("\n\nDollar comercial hoje:  R$", dolar.get_text())
