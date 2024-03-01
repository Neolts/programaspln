archivo_abierto=open("D:\\Programas\\Documentos\\Texto1.txt")
texto=archivo_abierto.read()
expresion_regular=re.compile(r"(el)?(los)? artículos?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
   print(resultado.group(0))
print(texto)
archivo_abierto.close()