import requests
import nltk
import re
import os
from bs4 import BeautifulSoup

def guardar_pagina (url, nombre_archivo):
    # Realizar la solicitud HTTP
    respuesta = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if respuesta.status_code == 200:
        # Analizar el HTML de la página web
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        
        # Obtener todo el texto de la página
        texto_pagina = soup.get_text()
        
        # Guardar el texto en un archivo
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(texto_pagina)
        print(f"La página web ha sido guardada en '{nombre_archivo}'.")
    else:
        print("Error al acceder a la página web.")
        
url_pagina = "https://concepto.de/cultura-olmeca/"
nombre_archivo = "pagina.txt"
guardar_pagina(url_pagina, nombre_archivo)

def contar_palabras_y_lineas(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            lineas = contenido.split("\n")
        num_palabras = len(palabras)
        num_lineas = len(lineas)
        print(f"Número de palabras: {num_palabras}")
        print(f"Número de líneas: {num_lineas}")
    except Exception as e:
        print(f"Error al contar palabras y líneas: {e}")

contar_palabras_y_lineas(nombre_archivo)

# Cargar el texto del archivo
archivo_nombre = "pagina.txt"
with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print("----------------------------------------------------------------------")

# Cargar palabras funcionales en español de NLTK
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)

print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print(tokens_limpios)
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

# Graficar las 40 palabras más comunes
distribucion_limpia.plot(20)