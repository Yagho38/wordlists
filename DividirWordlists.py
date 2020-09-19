from os import path, chdir, listdir, getcwd, system
import sys

with open("/home/yagho/Documentos/rockyou.txt") as results:
    original = results.readlines()
file2 = open('/home/yagho/Documentos/lista13.txt', 'w+')
counter = 0

for line in original:
    counter += 1
    if(counter >= 1200000 and counter <= 1300000):
        file2.write(line + '\n')
