import os , sys
import platform
work = os.getcwd()
from pathlib import Path

x = sys.argv[1]
tmp=(f"{work}/tmpdir")
osid = platform.system()
out=(f"{work}/out")
tdr= f"{work}/tools/bin/{osid}"
os.makedirs(f"{out}", exist_ok=True)

def make_img():
	filepath=Path(f"{tmp}/{x}")
	os.system(f"rm -rf {tmp}/config/{x}/{x}_size.txt")
	os.system(f'echo $(du -sb {tmp}/{x}) > size.txt ; expr $(cat size.txt | cut -d " " -f 1) + 200000000 > {tmp}/config/{x}/{x}_size.txt')
	if "odm" in x:
		os.system(f'echo $(du -sb {tmp}/{x}) > size.txt ;expr $(cat size.txt | cut -d " " -f 1) + 20000000 > {tmp}/config/{x}/{x}_size.txt; rm -rf size.txt')
	f = open(f'{tmp}/config/{x}/{x}_size.txt', 'r')
	size = f. read()
	print(f"Repacking {x}", size)
	os.system(f'{tdr}/make_ext4fs -T "1230768000" -S "{tmp}/config/{x}/{x}_file_contexts" -C "{tmp}/config/{x}/{x}_fs_config" -l "$(cat {tmp}/config/{x}/{x}_size.txt)" -a {x} {out}/{x}.img {tmp}/{x}/ > logs')
	f.close()
	os.system(f"rm -rf size.txt")

if __name__ == "__main__":
    make_img()
