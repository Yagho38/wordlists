#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys

url = sys.argv[1]
proxy = {'http': 'http://156.56.18.228:8080'}
dados = {"action": "polls",
	"view": "process",
	"poll_id": "2",
	"poll_2": "6",
	"poll_2_nonce": "af658e1b0e"
	}
cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

for i in range(1000):

	resposta = requests.post(url, headers=cabecalho, proxies=proxy, data=dados)
	print(i, " votos")
	print(resposta.text)
	
