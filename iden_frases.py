import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

# Asegúrate de haber descargado los datos necesarios de nltk
# Esto solo necesita hacerse una vez
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "NLTK es una biblioteca de Python para procesamiento de lenguaje natural."
words = word_tokenize(text)
tagged = nltk.pos_tag(words)
grammar = "NP: {<DT>?<JJ>*<NN>}"
parser = RegexpParser(grammar)
result = parser.parse(tagged)
print(result)
