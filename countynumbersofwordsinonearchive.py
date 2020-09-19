from os import path, chdir, listdir, getcwd, system
from zipfile import ZipFile
import sys

workingPath = getcwd()

#Check if Exiftool is installed and install it if not
exif_installed = system("exiftool >>/dev/null")
if exif_installed != 0:
    install = input("You don't have exiftool installed, would you like to install it? (Y/n): ")
    if install.lower() == "n":
        print("Program can't work without exiftool installed. Exiting...")
        sys.exit()
    
    system("sudo apt-get install exiftool -y")
    exif_installed = system("exiftool >>/dev/null")
    if exif_installed != 0:
        print("Fatal Error -- Couldn't install Exiftool. Check your repositories. Exiting...")
        sys.exit()
    print("\n\n\n\n\nProgram Starting Now:\n\n")

directory = "Downloads/extracted_files"
for i in listdir(directory):
    system(f"exiftool {directory}/{i} >> exiftool.txt")
with open("exiftool.txt") as etresults:
    metadata = etresults.readlines()
system("rm exiftool.txt")

counter = 0
for line in metadata:
    if "Version" in line and "1.1" in line:
        counter += 1
#Second answer:
print("The number of files containing Version: 1.1 is: ",counter)


