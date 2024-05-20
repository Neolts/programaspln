import nltk
nltk.download('punkt')

def riqueza_lexica(tokens):
   tokens_conjunto=set(tokens)
   palabras_totales=len(tokens)
   palabras_diferentes=len(tokens_conjunto)
   riqueza_lexica=palabras_diferentes/palabras_totales
   return riqueza_lexica

carpeta_nombre="C:\\Users\\Cristopher\\Downloads\\"
archivo_nombre="texto_n1.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")
riqueza_lexica=riqueza_lexica(tokens)
print(riqueza_lexica)

conteo_individual=tokens.count("el")
print(conteo_individual)
palabras_totales=len(tokens)
porcentaje=100*conteo_individual/palabras_totales
print("El porcentaje de la palabra es: " ,porcentaje,"%")