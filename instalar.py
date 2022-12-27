import os , sys

ruta = ":"+os.getenv('PATH')+"/YouTube_descarga"
os.chdir("..")
os.system("cp -rf YouTube_descarga /data/data/com.termux/files/usr/bin")
os.system("rm -rf YouTube_descarga")
fd = open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")
fd.write(f"alias youtube='cd /data/data/com.termux/files/usr/bin/YouTube_descarga &&  python youtube.py'")
fd.close()
