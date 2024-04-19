import docx2txt
import nltk
import re
import os

def convertir_word_a_txt(archivo_word, archivo_txt):
    try:
        texto = docx2txt.process(archivo_word)
        with open(archivo_txt, "w", encoding="utf-8") as archivo_salida:
            archivo_salida.write(texto)
        print("Archivo convertido exitosamente.")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")

# Rutas de los archivos
archivo_word = " invest_.docx"
archivo_txt = "texto_docx1.txt"

# Convertir archivo Word a archivo de texto
convertir_word_a_txt(archivo_word, archivo_txt)

def contar_palabras_y_lineas(archivo_txt):
    try:
        with open(archivo_txt, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            lineas = contenido.split("\n")
        num_palabras = len(palabras)
        num_lineas = len(lineas)
        print(f"Número de palabras: {num_palabras}")
        print(f"Número de líneas: {num_lineas}")
    except Exception as e:
        print(f"Error al contar palabras y líneas: {e}")
contar_palabras_y_lineas(archivo_txt)

# Cargar el texto del archivo
archivo_nombre = "texto_docx1.txt"
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