from os import path, chdir, listdir, getcwd, system
from zipfile import ZipFile
import sys

chdir("Downloads/extracted_files")
for filename in listdir():
    try:
        with open(filename, "r") as f:
            data = f.read()
            if "password" in data:
                print("Filename is: ", filename)
    except:
        continue
