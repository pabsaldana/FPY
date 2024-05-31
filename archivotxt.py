datos="""yo cree el archivo y tendra lindo testo
cd d:\ se cambia la ruta de donde se guarda el archivo
"""
#w escritura
#r lectura
#r+ lectura/escritura
with open('texto.txt', 'w') as archivo:
    archivo.write(datos)

#opcion 1 leer
archivo=open('texto.txt', 'r')
contenido=archivo.read()
print(contenido)
archivo.close()

#opcion 2 leer
with open('texto.txt', 'r') as archivo:
    contenido=archivo.read()
print(contenido)
