from bs4 import BeautifulSoup
import requests
import re
import base64
import json
import pymysql
import time
import threading

catego = [94, 95, 1, 96, 97, 98, 101, 104, 105, 106, 107, 108, 111, 112, 113, 114, 115, 116, 118, 119, 120, 122, 123, 124, 125, 127, 128, 130, 131, 132, 133]

nick = ['amateur', 'anal', 'asian', 'asmr', 'bbw', 'bi', 'big_cock', 'black', 'blonde', 'blowjob', 'brunette', 'cam_porn', 'creampie', 'cumshot', 'fisting', 'fucked_up_family', 'gangbang', 'gapes', 'indian', 'interracial', 'latina', 'lesbian', 'lingerie', 'mature', 'milf', 'oiled', 'redhead', 'solo', 'squirting', 'stockings', 'teen']

urlx = ['Amateur-65', 'Anal-12', 'Asian_Woman-32', 'ASMR-229', 'bbw-51', 'Bi_Sexual-62', 'Gay_big_cock-105', 'Black_Woman-30', 'Blonde-20', 'Blowjob-15', 'Brunette-25', 'Cam_Porn-58', 'Creampie-40', 'Cumshot-18', 'Fisting-165', 'Fucked_Up_Family-81', 'Gangbang-69', 'Gapes-167', 'Indian-89', 'Interracial-27', 'Latina-16', 'Lesbian-26', 'Lingerie-83', 'Mature-38', 'Milf-19', 'Oiled-22', 'Redhead-31', 'Solo_and_Masturbation-33', 'Squirting-56', 'Stockings-28', 'Teen-13']


for bj in range(len(urlx)):

	i = 0
	j = 0
	urls = 0
	urlbase = str(urlx[bj])
	numerodepaginas = 5
	numerocategorias = int(catego[bj])
	to_crawl = [f'https://www.xvideos.com/c/{urlbase}']
	for pg in range(numerodepaginas):
		to_crawl.append(f'https://www.xvideos.com/c/{urlbase}/{(pg + 1)}')
	thumbs = []
	titles = []
	categories = []
	sites = []
	hd = []
	htmllink2 = []
	cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
	ursl = "http://pynporn.com/?rest_route=/wp/v2"
	user = "YagDesck"
	senha = "XdEZ U4fl Di7Z TPki 2sV7 bVD8"

	credenciais = user + ':' + senha 

	token = base64.b64encode(credenciais.encode())

	header = {'Authorization': 'Basic ' + token.decode('utf-8')}
	categoria = str(urlbase).split("-")[0]
	if "_" in categoria:
		categoria = categoria.replace("_", " ")

	def pegartodos():
		for k in to_crawl:
			url = str(k)
			try:
				req = requests.get(url, headers=cabecalho)
			except:
				continue
			html = req.text

			soup = BeautifulSoup(html, 'html.parser')

			pegado = soup.find_all(class_="thumb")
			for item in pegado:
				hreflink = item.a['href']
				htmllink = f'https://www.xvideos.com{hreflink}'
				htmllink2.append(htmllink)
				print(htmllink)
		print('\n\n\n\n\n\n\n\n-------------------------------')
	pegartodos()
	def acharcoisas(olinka):
		url = htmllink2[olinka]
		req = requests.get(url, headers=cabecalho)
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		intitulo = soup.find(class_="page-title")
		urlvideolow = re.findall(r'https?:\/\/[^"\'>]*', html)
		urlvideohigh = re.findall(r'setVideoUrlHigh', html)
		if len(urlvideohigh) != 0:
			urlvideo = urlvideolow[36]
			hd.append("on")
			thumb = urlvideolow[39]
		else:
			urlvideo = urlvideolow[35]
			hd.append("off")
			thumb = urlvideolow[37]
		req = requests.get(thumb, headers=cabecalho)
		if req.status_code != 404:
			sites.append(urlvideo)
			thumbs.append(thumb)
			titulo = str(intitulo.get_text()).split(" ")[:-3]
			titulo = ' '.join(map(str, titulo))
			eleehd = str(intitulo.get_text()).split(" ")[-1:]
			titles.append(titulo)
			print("\n\n\n", olinka + 1, "ok")
		else:
			print("\n\n\n", olinka + 1, "deu ruim")


	def postar(z):
		if z == 0:
			thr = []
			for c in range(len(htmllink2) - 1):
				th = threading.Thread(target=acharcoisas, args=(c, ))
				thr.append(th)
				if c != 0:
					if thr[c - 2].is_alive():
						time.sleep(.300)
					th.start()
				else:
					th.start()
				while thr[c].is_alive():
					pass
				
		else:
			print("\n\n", z, "\n")
			print("URL:", sites[z - 1])
			print("Thumb", thumbs[z - 1])
			print("Titulo", titles[z - 1])
			print("Categoria", categoria)
			print("HD", hd[z - 1])
			post = {'title': f'{titles[z - 1]}',
				'content': f'{titles[z - 1]}' + f'<!-- {htmllink2[z - 1]} -->',
				'status': 'publish',
				'categories': f'{numerocategorias}',
				}
			update = requests.post(ursl + '/posts/', headers=header, json=post)
			print(update)

			conexao = pymysql.connect(db='wordpress', user='root', passwd='JUJuba123456')

			cursor = conexao.cursor()

			
			postid = cursor.execute(f"SELECT * FROM wp_posts") 
			
			result = cursor.fetchall()
			oid = str(result[len(result) - 1]).split(",")[0]
			oid2 = int(oid[1:])
			postid = cursor.execute(f"SELECT * FROM wp_postmeta")
			result2 = cursor.fetchall()
			oid3 = str(result2[len(result2) - 1]).split(",")[0]
			oid4 = int(oid3[1:])
			
			cursor.execute(f"INSERT INTO `wp_postmeta` (`meta_id`, `post_id`, `meta_key`, `meta_value`) VALUES ('{oid4 + 1}', '{oid2 + 1}', 'video_url_720', '{sites[z]}\r\n');")
			cursor.execute(f"INSERT INTO `wp_postmeta` (`meta_id`, `post_id`, `meta_key`, `meta_value`) VALUES ('{oid4 + 2}', '{oid2 + 1}', 'thumb', '{thumbs[z - 1]}\r\n');")
			cursor.execute(f"INSERT INTO `wp_postmeta` (`meta_id`, `post_id`, `meta_key`, `meta_value`) VALUES ('{oid4 + 3}', '{oid2 + 1}', 'hd_video', '{hd[z - 1]}\r\n');")
			print(oid2)
			conexao.commit()


			conexao.close()

	for f in range(len(htmllink2) - 1):
		postar(f)
