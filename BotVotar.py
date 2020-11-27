#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys
import ssl
import urllib2

target = "https://voting-vote-producer.r7.com/vote"
data = "voting_id=271&alternative_id=657"
context = ssl._create_unverified_context()
cabecalho = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
req = urllib2.Request(target,data,headers=cabecalho)

for i in range(1000):
	res = urllib2.urlopen(req, context=context)
	print(i, " votos")
	print(res)
	
