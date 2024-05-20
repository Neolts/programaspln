from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# Texto de ejemplo en español
texto = "Hoy a sido una muy buena semana"

# Crear un objeto TextBlob para el texto en español
blob_es = TextBlob(texto, analyzer=NaiveBayesAnalyzer())

# Obtener la polaridad del sentimiento
polarity = blob_es.sentiment.p_pos - blob_es.sentiment.p_neg

# Clasificar el sentimiento como positivo, negativo o neutral
if polarity > 0:
    sentiment = "positivo"
elif polarity < 0:
    sentiment = "negativo"
else:
    sentiment = "neutral"

# Imprimir los resultados
print("Texto:", texto)
print("Sentimiento:", sentiment)
