from os import path, chdir, listdir, getcwd, system
from zipfile import ZipFile
import sys

workingPath = getcwd()

if len(sys.argv): 

	with ZipFile(workingPath+"/"+sys.argv[1], 'r') as zipfile:
    		zipfile.extractall(workingPath+"/extracted_zips")
	for zfile in listdir(workingPath + "/extracted_zips"):
    		with ZipFile(workingPath+"/extracted_zips/"+zfile) as zipfile:
            		zipfile.extractall(workingPath+"/extracted_files")
	print("The number of files is: ",len(listdir(workingPath+"/extracted_files")))
