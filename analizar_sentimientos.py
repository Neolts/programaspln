import nltk
from transformers import pipeline

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar el léxico VADER
nltk.download('vader_lexicon')

# Inicializar el analizador
sia = SentimentIntensityAnalyzer()

# Texto de ejemplo
texto = "What nice weather we have today isn't?."

# Obtener las puntuaciones de sentimiento
scores = sia.polarity_scores(texto)

# Imprimir los resultados
print(scores)



