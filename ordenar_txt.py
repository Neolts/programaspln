import re
carpeta_nombre="D:\\Programas\\Documentos\\" 
archivo_nombre="Texto1.txt" 
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read() 
palabras_lista=texto.split() 
palabras_lista.sort() 
for palabra in palabras_lista: 
    print(palabra)  
