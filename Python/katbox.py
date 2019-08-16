import json
with open("catz.txt", 'r') as archivoCatz:
        for linea in archivoCatz:
            print("printf("+json.dumps(line)+");")

