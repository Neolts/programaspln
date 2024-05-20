import pyttsx3

def texto_a_audio(texto, nombre_archivo):
    motor_tts = pyttsx3.init()
    motor_tts.save_to_file(texto, nombre_archivo)
    motor_tts.runAndWait()

# Texto que se convertirá a audio
texto = "Hola, este es un ejemplo de texto convertido a audio."

# Nombre del archivo de audio de salida
nombre_archivo_audio = "texto_convertido.wav"

# Convertir texto a audio
texto_a_audio(texto, nombre_archivo_audio)

print("Texto convertido a audio y guardado como:", nombre_archivo_audio)
