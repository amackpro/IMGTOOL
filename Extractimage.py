#!/usr/bin/env python3
from asyncore import file_dispatcher
import sys , os , os.path
import wget , shutil , time
import platform

from zipfile import ZipFile
from pathlib import Path

seconds = time.time()
osid = platform.system()
work = os.getcwd()
tmp=(f"{work}/tmpdir")
tooldir= f"{work}/tools"
tdr = f"{tooldir}/bin/{osid}"
os.makedirs(f"{tmp}", exist_ok=True)
img = sys.argv[1]

def img_ext(img):
	filepath = Path(f"{img}")
	if filepath.exists():
		print(f"       Unpacking Image ")
		os.system(f"python {tooldir}/py/imgextractor.py {img} tmpdir >> logs")
		if f"{tmp}" in img:
	        	os.remove(f"{img}")

	
def checker():
	filepath = Path(sys.argv[1])
	if filepath.exists():
		if "super" in sys.argv[1]:
			print("Super image detected , Extracting only super image")
			os.system(f"python {tooldir}/py/lpunpack.py {img} {tmp}/")
			os.remove(f"super.unsparse.img")
			exit()
	img_ext(img)

if __name__ == "__main__":
    checker()

