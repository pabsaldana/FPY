import json
datos ={
    "nombre":"Esteban",
    "edad":25,
    "comuna":"Santiago",
    "estudios":["Colegio Arturo Prat","Liceo el Bosque",
                "DuocUC","Diplomados DuocUC","Cato"]
    }
with open('archivo.json','w') as archivo:
    json.dump(datos, archivo)
with open('archivo.json','r') as archivo:
    leer=json.load(archivo)
    print(leer)