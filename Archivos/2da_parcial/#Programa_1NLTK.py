#Programa_1NLTK
import re
import nltk

carpeta_nombre="C:\\Users\\Cristopher\\Downloads\\"
archivo_nombre="texto_n1.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
 texto=archivo.read()

expresion_regular=re.compile(r"...? ")

resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
 print(resultado.group(0))
