
import os 
import re

os.system("pause")
carpeta_nombre="Documentos\\"
archivo_nombre="Texto1.txt"

txt=("D:\\programaspln\\Archivos\\1ra Parcial\\Documentos\\Texto_1_1.txt")

expresion_regular=re.compile(r"(el)?(los)? artículos?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
   print(resultado.group(0))
print(texto)
archivo_abierto.close()