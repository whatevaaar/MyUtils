#Extractor
import glob
import os
import sys

#Signo para los directorios dependiendo del so
signoDir = '/' if (os.name == "posix") else '\\'
directorio = os.getcwd() if len(sys.argv) < 2  else sys.argv[1:]
print(directorio)
archivos = [x for x in glob.glob(directorio + signoDir + "**" + signoDir + "*.*")]
for archivo in archivos:
    os.rename(archivo, directorio + signoDir + os.path.basename(archivo))
print(archivos)
