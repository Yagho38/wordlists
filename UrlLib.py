import urllib3

url = 'http://solyd.com.br'

cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

http = urllib3.PoolManager()
r = http.request('GET', url, headers=cabecalho)

print(r.status)
