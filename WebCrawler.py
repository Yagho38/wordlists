import re
import requests

to_crawl = ['http://uhcv19-final.uhc.seg.br/0']

crawled = set()
cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
while True:
	url = to_crawl[0]
	try:
		req = requests.get(url, headers=cabecalho)
	except:
		to_crawl.remove(url)
		crawled.add(url)
		continue
	html = req.text
	print("Crawling: ", url)

	links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)

	to_crawl.remove(url)
	crawled.add(url)

	for link in links:
		if link not in crawled and link not in to_crawl:
			if "uhcv" in link:
				to_crawl.append(link)
			else:
				continue
