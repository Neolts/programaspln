import PyPDF2
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Descargar el tokenizador punkt de NLTK si no lo has hecho antes
nltk.download('punkt')

# Función para extraer texto de un archivo PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text += page.extract_text()
    return text

# Ruta al archivo PDF que quieres convertir
pdf_path = 'escalar_red.pdf'

# Extraer texto del archivo PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Tokenizar el texto en palabras
tokens = word_tokenize(pdf_text)

# Contar el número de palabras
num_words = len(tokens)

# Tokenizar el texto en oraciones para contar líneas
sentences = sent_tokenize(pdf_text)

# Contar el número de líneas
num_lines = len(sentences)

# Guardar los tokens en un archivo de texto
with open('texto_extraido.txt', 'w', encoding='utf-8') as file:
    file.write(pdf_text)

# Imprimir el número de palabras y líneas
print("Número de palabras:", num_words)
print("Número de líneas:", num_lines)
