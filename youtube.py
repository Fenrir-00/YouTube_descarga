import os, sys, time
while True:
 try:
  from pytube import YouTube
  break
 except ModuleNotFoundError:
  os.system("pip install pytube")
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")
while True:
 try:
  import requests
  break
 except ModuleNotFoundError:
  os.system("pip install requests")
r= requests.get("https://raw.githubusercontent.com/Fenrir-00/YouTube_descarga/main/version.txt")
r=r.text
print(r)
if r != "version=1.2\n":
 os.system("clear")
 print(f"""{color.rojo}HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO
HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO""")
 time.sleep(5)


class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'



def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝""")
 print(f"{color.fin}")
def cabecera():
 os.system("clear")
 print(f"""{color.cyan}

██╗   ██╗ █████╗ ██╗   ██╗████████╗███╗  ░███╗██╗   ██╗██╗  ██╗
╚██╗ ██╔╝██╔══██╗██║   ██║╚══██╔══╝████╗ ████║██║   ██║╚██╗██╔╝
 ╚████╔╝ ██║  ██║██║   ██║   ██║   ██╔████╔██║██║   ██║ ╚███╔╝
  ╚██╔╝  ██║  ██║██║   ██║   ██║   ██║╚██╔╝██║██║   ██║ ██╔██╗
   ██║   ╚█████╔╝╚██████╔╝   ██║   ██║ ╚═╝ ██║╚██████╔╝██╔╝╚██╗
   ╚═╝    ╚════╝  ╚═════╝    ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝""")
def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  1.2                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)
 print()

def carga():
    print(f"{color.verde}")
    print("""Loading…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    banner()
def incorrecto():
    os.system("clear")
    print(f"""{color.rojo}
░█████╗░██████╗░░█████╗░██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
██║░░██║██████╔╝██║░░╚═╝██║██║░░██║██╔██╗██║
██║░░██║██╔═══╝░██║░░██╗██║██║░░██║██║╚████║
╚█████╔╝██║░░░░░╚█████╔╝██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝
██╗███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
██║████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║░░╚═╝██║░░██║██████╔╝██████╔╝
██║██║╚████║██║░░██╗██║░░██║██╔══██╗██╔══██╗
██║██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██║░░██║
╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
███████╗░█████╗░████████╗░█████╗░
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗░░██║░░╚═╝░░░██║░░░███████║
██╔══╝░░██║░░██╗░░░██║░░░██╔══██║
███████╗╚█████╔╝░░░██║░░░██║░░██║
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝{color.fin}""")
    time.sleep(4)
    menu()
def salir():
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    print(f"{color.fin}")
    sys.exit()

def menu():
    os.system("clear")
    cabecera()
    version()
    print(f"{color.morado} DESCARGA  VIDEOS DE YOUTUBE{color.fin}")
    print("")
    print(f"{color.cyan}QUE TE GUSTARIA HACER{color.fin}")
    print(f"{color.verde}[1]DESCARGAR VIDEO")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
     descargar()
    elif eleccion == "0" :
     banner()
     salir() 
    else:
        incorrecto()

def descargar():
 banner()
 print()
 print(f"{color.morado} DESCARGA  VIDEOS DE YOUTUBE{color.fin}")
 print()
 url = input("PEGA EL ENLACE DEL VIDEO >> ")
 print(f"{color.amarillo} TARDARA DEPENDIENDO DE LA DURACION DEL VIDEO{color.fin}")
 yt = YouTube(url)
 yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
 os.system("mv *mp4 /data/data/com.termux/files/home/storage/downloads")
 banner()
 print(f"{color.verde} VIDEO DESCARGADO EN LA CARPETA DOWNLOADS DE TU TELEFONO{color.fin}")
 time.sleep(4)
 menu()

menu()
