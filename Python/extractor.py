#Extractor
import glob
import os
import sys

#Signo para los directorios dependiendo del so
signoDir = '/' if (os.name == "posix") else '\\'
directorio = os.getcwd()
archivos = [x for x in glob.glob(directorio + signoDir + "**" + signoDir + "*.*",recursive=True)]

for archivo in archivos:
    os.rename(archivo, directorio + signoDir + os.path.basename(archivo))

