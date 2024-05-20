#Programa_2NLTK
import nltk
import matplotlib.pyplot as plt
carpeta_nombre="C:\\Users\\Cristopher\\Downloads\\"
archivo_nombre="texto_n1.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
 texto=archivo.read()
print("----------------------------------------------------------------------")
tokens=nltk.word_tokenize(texto, "spanish")

tokens_conjunto=set(tokens)
palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)
print(palabras_totales)
print(palabras_diferentes)
texto_nltk=nltk.Text(tokens)
distribucion=nltk.FreqDist(texto_nltk)
print("----------------------------------------------------------------------")
hapaxes=distribucion.hapaxes()
for hapax in hapaxes:
 print(hapax)
from matplotlib import rcParams
rcParams.update({"figure.autolayout": True})
distribucion.plot(cumulative=True)