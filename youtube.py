#!/usr/bin/env python
import os
import  sys
import  time

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

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

r= requests.get("https://raw.githubusercontent.com/Fenrir-00/YouTube_descarga/main/version.txt")
r=r.text
if r != "version=1.3\n":
 os.system("clear")
 print((color.rojo + ('HAY UNA NUEVA VERSION ACTUALIZA EL REPOSITORIO\n') * 20))
 input(f"{color.cyan} PULSA CUALQUIER TECLA PARA SEGUIR >>")





def banner():
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
 | Version                : Version  1.3                 |
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
 █████╗ ██████╗  █████╗ ██╗ █████╗ ███╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗ ██║
██║  ██║██████╔╝██║  ╚═╝██║██║  ██║██╔██╗██║
██║  ██║██╔═══╝ ██║  ██╗██║██║  ██║██║╚████║
╚█████╔╝██║     ╚█████╔╝██║╚█████╔╝██║ ╚███║
 ╚════╝ ╚═╝      ╚════╝ ╚═╝ ╚════╝ ╚═╝  ╚══╝
██╗███╗  ██╗ █████╗  █████╗ ██████╗ ██████╗
██║████╗ ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║  ╚═╝██║  ██║██████╔╝██████╔╝
██║██║╚████║██║  ██╗██║  ██║██╔══██╗██╔══██╗
██║██║ ╚███║╚█████╔╝╚█████╔╝██║  ██║██║  ██║
╚═╝╚═╝  ╚══╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
███████╗ █████╗ ████████╗ █████╗
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗  ██║  ╚═╝   ██║   ███████║
██╔══╝  ██║  ██╗   ██║   ██╔══██║
███████╗╚█████╔╝   ██║   ██║  ██║
╚══════╝ ╚════╝    ╚═╝   ╚═╝  ╚═╝{color.fin}""")
    time.sleep(4)
    menu()

def salir():
    os.system("clear")
    banner()
    version()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    version()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    version()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    version()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    version()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    version()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    print(f"{color.fin}")
    sys.exit()

def menu():
    os.system("clear")
    banner()
    version()
    print(f"{color.morado} DESCARGA  VIDEOS DE YOUTUBE{color.fin}")
    print("")
    print(f"{color.cyan}QUE TE GUSTARIA HACER{color.fin}")
    print(f"{color.verde}[1]DESCARGAR VIDEO")
    print(f"{color.verde}[2]VER VIDEO")
    print(f"{color.amarillo}[3]AYUDA")
    print(f"{color.rojo}[0]SALIR{color.fin}")
    eleccion =input(f"{color.cyan}ELIJE UN NUMERO >>{color.fin} ")
    if eleccion == "1" :
     descargar()
    elif eleccion =="2":
     reproductor()
    elif eleccion =="3":
     ayuda()
    elif eleccion == "0" :
     banner()
     salir() 
    else:
        incorrecto()

def descargar(arg1=None):
 if arg1 == None:
  banner()
  print()
  print(f"{color.morado} DESCARGA  VIDEOS DE YOUTUBE{color.fin}")
  print()
  url = input("PEGA EL ENLACE DEL VIDEO >> ")
 else : url = arg1
 print(f"{color.amarillo} TARDARA DEPENDIENDO DE LA DURACION DEL VIDEO{color.fin}")
 yt = YouTube(url)
 yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
 os.system("mv *mp4 /data/data/com.termux/files/home/storage/downloads")
 banner()
 version()
 print(f"{color.verde} VIDEO DESCARGADO EN LA CARPETA DOWNLOADS DE TU TELEFONO{color.fin}")
 input(f"{color.cyan} PULSA CUALQUIER TECLA PARA SEGUIR >>")
 if arg1 == None:
  menu()
 else :
  exit()

def reproductor():
 banner()
 version()
 ruta = "/data/data/com.termux/files/home/storage/downloads"
 os.chdir(ruta)
 if os.path.exists(ruta):
    archivos = os.listdir(ruta)
    archivos_mp4 = [archivo for archivo in archivos if archivo.lower().endswith('.mp4')]
    print(f"""{color.morado}
 LISTADO DE VIDEOS{color.verde}""")
    for indice, archivo in enumerate(archivos_mp4, start=1):
        print(f"{indice}. {archivo}")

    
    numero_elegido = input(f"{color.cyan}ELIJE UN NUMERO DE VIDEO PARA REPRODUCIRLO >>  ")

    try:
        numero_elegido = int(numero_elegido)
        if 1 <= numero_elegido <= len(archivos_mp4):
            nombre_video = archivos_mp4[numero_elegido - 1]
            video = nombre_video
            html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Página de Reproducción de Video</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            overflow: hidden;
        }}
        video {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
    </style>
</head>
<body>
    <video autoplay controls preload="auto">
        <source src="{video}" type="video/mp4">
        Tu navegador no soporta la reproducción de videos.
    </video>
</body>
</html>
"""

            with open('index.html', 'w') as file:
             file.write(html_content)

            try:
              os.system("php -S localhost:8080 &>/dev/null & clear")
              os.system("termux-open-url http://localhost:8080")
              while True:
               banner()
               version()
               print(f"{color.verde}reproduciendo video")
               print(f"{color.cyan}pulsa CTRL C para salir{color.fin}")
               time.sleep(60)
            except KeyboardInterrupt:
               os.system("php_server_process.terminate()")
               os.system("php_server_process.wait()")
               os.system("rm index.html")
               menu()
        else:
            incorrecto()
    except ValueError:
        incorrecto()

 else:
    incorrecto()


def ayuda():
 banner()
 version()
 print(f"""{color.verde}
              BIENVENIDO AL PANEL DE AYUDA

 Es  un script dedicado a descargar videos de youtube
 podemos verlos desde termux o con tu reprodcutor ya
 qie se guardan en tu carpeta descagargas de tu telefono

 USO CON INTERFAZ GRAFICA :
 ejemplos: python youtube.py

 USO RAPIDO :
 ejemplos: python youtube.py https://youtu.be/b2_b_Y0N_6o?si=EcMJogoFg-URd4GI
{color.fin}""")

def main():
    arg=sys.argv
    if len(arg) == 1:
     menu()
    else:
     if "-h" in arg or "--help" in arg or "help" in arg or "-help" in arg:
       ayuda()
     else:
      url = str(sys.argv[1:])
      url = url.strip("[]")
      descargar(url)

if __name__ == "__main__":
    main()

