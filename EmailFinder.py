import re
import requests

to_crawl = ['https://github.com']
emails_found = set()

crawled = set()
cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
for i in range(10):
	url = to_crawl[0]
	
	try:
		req = requests.get(url, headers=cabecalho, timeout=20.0)
	except:
		to_crawl.remove(url)
		crawled.add(url)
		continue
	html = req.text
	print("Crawling: ", url)

	links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)

	emails = re.findall(r'[\w\._-]+@[\w_-]+\.[\w\._-]+\w', html)
	
	to_crawl.remove(url)
	crawled.add(url)

	for link in links:
		if link not in crawled and link not in to_crawl:
			to_crawl.append(link)
	for email in emails:
		emails_found.add(email)

print("--------------------------------------------\n\nEMAILS ENCONTRADOS:\n")
for j in emails_found:
	print(j)

	
