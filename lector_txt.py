import pyttsx3

def texto_a_audio(nombre_archivo_entrada, nombre_archivo_salida):
    motor_tts = pyttsx3.init()

    with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo_entrada:
        texto = archivo_entrada.read()

    motor_tts.save_to_file(texto, nombre_archivo_salida)
    motor_tts.runAndWait()

    # Reproducir el texto en el momento
    motor_tts.say(texto)
    motor_tts.runAndWait()

# Nombre del archivo de texto de entrada
nombre_archivo_texto = "texto_entrada.txt"

# Nombre del archivo de audio de salida
nombre_archivo_audio = "texto_convertido.wav"

# Convertir texto a audio y reproducirlo
texto_a_audio(nombre_archivo_texto, nombre_archivo_audio)

print("Texto convertido a audio y guardado como:", nombre_archivo_audio)
