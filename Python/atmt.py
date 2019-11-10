with open ('/home/nexus/Code/Python/Automata/data.txt',w) as dataFile:
    archivo = dataFile.readlines()
    archivo = [linea.strip() for linea in archivo]
    estados = archivo[0]
    lenguaje = archivo[1]
    estadoInicial = archivo[2]
    estadoFinal = archivo[3]
    reglas = [linea for linea in archivos[3:]]
    print("Estados: " + estados + "\nLenguaje: " lenguaje + "\nEstado Inicial " + estadoInicial + "\nEstado Final: " + estadoFinal)
