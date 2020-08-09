

from os import path, chdir, listdir, getcwd, system
import sys


archive = "Downloads/oie.txt"
#system(f"cat {archive} >> emails.txt")
with open("Downloads/oie.txt") as results:
    metadata = results.readlines()
counter = 0
counter2 = 0
counter3 = 0
for line in metadata:
    if ".com" in line and "@" in line:
        print(line)
        counter2 += 1
        counter += 1
    counter2 += 2
    counter2 = counter2 % 2
    if counter3 == 1:
        print(line)
        counter3 = 0
    if counter2 == 1:
        counter3 = 1
        counter2 += 1
print("The number of emails captured by keylogger is: ",counter)


