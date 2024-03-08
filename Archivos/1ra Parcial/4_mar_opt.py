import nltk
nltk.download('punkt')

carpeta_nombre="C:\\Users\\Cristopher\\Downloads\\"
archivo_nombre="texto_n1.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print(token)

print("\n\n")
palabras_total=len(tokens)
print(palabras_total) 
## Riqueza Lexica ##
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print("Riqueza Lexica")
print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
tokens_conjunto=set(tokens)
palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)
riqueza_lexica=palabras_diferentes/palabras_totales
print(riqueza_lexica)
print("Adicion")