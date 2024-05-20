import os 

os.system("pause")
carpeta_nombre="Documentos\\"
archivo_nombre="Texto1.txt"

txt=("D:\\programaspln\\Archivos\\1ra Parcial\\Documentos\\Texto_1_1.txt")

with open(txt,"r") as archivo:
     texto=archivo.read()
print(texto)

