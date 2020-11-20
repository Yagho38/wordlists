import re
import requests

to_crawl = ['http://testphp.acunetix.com/listproducts.php?cat=1']

crawled = set()
cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

url = to_crawl[0]
padrao = re.search(r'(\?[\w:/\._-]+=)([\w:/\._-]+)', url)

injecao = padrao.groups()[0] + r"'"
try:
	req = requests.get(injecao, headers=cabecalho)
except:
	print('nao funcionou')
	continue
html = req.text
print("Crawling: ", url)
if 'mysql_fetch_array()' in html:
	print('vuneravel')
else:
	print('não é vuneravel')
