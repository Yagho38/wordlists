# -*- coding: utf-8 -*-

from os import path, chdir, listdir, getcwd, system
import sys

with open("/usr/share/wordlists/rockyou.txt", "r") as results:
    original = results.readlines()
nomeDoArquivo = str(raw_input("Nome do arquivo: "))
numero1 = int(input("Digite o numero inicial: "))
numero2 = int(input("Digite o numero final: "))
file2 = open(("/home/hack/Documentos/" + str(nomeDoArquivo)), "w+")
counter = 0
for line in original:
    counter += 1
    if(counter >= numero1 and counter <= numero2):
        file2.writelines(line)
