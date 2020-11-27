from os import path, chdir, listdir, getcwd, system
from zipfile import ZipFile
import sys

chdir("html")
for filename in listdir():
    try:
        with open(filename, "r") as f:
            data = f.read()
            if "THM" in data:
                print("Filename is: ", filename)
    except:
        continue
