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

def obtener_direccion_archivo():
    while True:
        direccion_archivo = input("Por favor, introduce la dirección del archivo Word: ")
        if os.path.exists(direccion_archivo):
            return direccion_archivo
        else:
            print("El archivo no existe. Por favor, introduce una dirección válida.")

# Obtener la dirección del archivo Word
archivo_word = obtener_direccion_archivo()
archivo_txt = "texto_docx5.txt"

# Convertir archivo Word a archivo de texto
convertir_word_a_txt(archivo_word, archivo_txt)

# Contar palabras y líneas en el archivo de texto
contar_palabras_y_lineas(archivo_txt)

# Cargar el texto del archivo
with open(archivo_txt, "r", encoding="utf-8") as archivo:
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

# Graficar las 20 palabras más comunes
distribucion_limpia.plot(20)
