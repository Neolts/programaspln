import nltk
nltk.download('punkt')

carpeta_nombre="Documentos\\"
archivo_nombre="texto_n1.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print(token)

print("\n\n")
palabras_total=len(tokens)
print(palabras_total)