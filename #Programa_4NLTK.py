#Programa_4NLTK
import os
import re

carpeta_nombre="C:\\Users\\Cristopher\\Downloads\\"
archivos_lista=os.listdir(carpeta_nombre)

expresion_regular=re.compile(r"\.docx?$")

for archivo_nombre in archivos_lista:
  resultado_busqueda=expresion_regular.search(archivo_nombre)
  if resultado_busqueda:
   print(resultado_busqueda.group(0))
   print(archivo_nombre)