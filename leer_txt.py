import os 

os.system("pause")
carpeta_nombre="Documentos\\"
archivo_nombre="Texto1.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
     texto=archivo.read()
print(texto)

