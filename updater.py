import pymysql
import requests
import re
import threading
	
lista = []
lista2 = []
lista3 = []
sites = []
hd = []
cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
conexao = pymysql.connect(db='wordpress', user='root', passwd='JUJuba123456')

cursor = conexao.cursor()
categoid = cursor.execute(f"SELECT * FROM wp_term_relationships") 
result = cursor.fetchall()
postid = cursor.execute(f"SELECT * FROM wp_posts") 
result2 = cursor.fetchall()
for i in result:
	for j in result2:
		oid = str(i).split(",")[0]
		oid2 = int(oid[1:])
		oid3 = str(i).split(",")[1]
		oid4 = str(j).split(",")[0]
		oid5 = int(oid4[1:])
		#print(i)
		if len(str(oid2)) > 4 and str(oid2) in str(oid5):
			lista.append(oid2)
print("oid2 ok")
q = "SELECT post_content FROM wp_posts"
postid1 = cursor.execute(q) 
result3 = cursor.fetchall()
for k in result3:
	if "xvideos" in str(k):
		vari = str(str(k).split("<")[1]).split(" ")[1]
		lista2.append(vari)	
print("vari ok")
def aqui(l):
	print("entrando em", lista2[l])
	url = str(lista2[l])
	try:
		req = requests.get(url, headers=cabecalho)
		html = req.text
		urlvideolow = re.findall(r'https?:\/\/[^"\'>]*', html)
		urlvideohigh = re.findall(r'setVideoUrlHigh', html)
	except:
		urlvideolow = []
		pass
		urlvideohigh = "notmano"
		for v in range(0, 36):
			urlvideolow.append("notmano")
	if len(urlvideolow) > 35:
		if len(urlvideohigh) != 0:
			urlvideo = urlvideolow[36]
			hd.append("on")
		else:
			urlvideo = urlvideolow[35]
			hd.append("off")
	else:
		urlvideo = "offline"
	print("pegando", urlvideo)
	if "xvideos" in str(urlvideo):
		sites.append(urlvideo)
		print(l + 1, "ok", "\n\n\n\n")
	else:
		print("esse não foi")
		sites.append("Offline")

thr = []
for m in range(len(lista2) - 1):
	th = threading.Thread(target=aqui, args=(m, ))
	thr.append(th)
	if m != 0:
		if thr[m - 2].is_alive():
			time.sleep(.300)
		th.start()
	else:
		th.start()
	while thr[m].is_alive():
		pass
	

print(len(lista))
print(len(lista2))
for n in lista:
	q = f"SELECT meta_id FROM wp_postmeta WHERE post_id = {n}"
	postid2 = cursor.execute(q) 
	result4 = cursor.fetchall()
	pegadon = str(str(str(result4).split(")")[0])[2:])[:-1]
	lista3.append(pegadon)
lista3.pop(0)
print(lista3)
for o in range(len(lista3) - 1):
	q = "UPDATE wp_postmeta SET meta_value = '" + sites[o] + "' WHERE meta_id = '" + lista3[o] + "'"
	print(q)
	postid3 = cursor.execute(q)

conexao.commit()


conexao.close()
