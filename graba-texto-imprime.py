import pyaudio
import speech_recognition as sr

def grabar_y_convertir_audio():
    formato = pyaudio.paInt16
    canales = 1
    tasa_muestreo = 44100
    tamano_buffer = 1024
    duracion_grabacion = 8
    nombre_archivo = "audio.wav"

    audio = pyaudio.PyAudio()

    stream = audio.open(format=formato, channels=canales, rate=tasa_muestreo, input=True, frames_per_buffer=tamano_buffer)

    print("Grabando audio...")

    frames = []

    for i in range(0, int(tasa_muestreo / tamano_buffer * duracion_grabacion)):
        data = stream.read(tamano_buffer)
        frames.append(data)

    print("Grabación finalizada.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    reconocedor = sr.Recognizer()

    audio_grabado = sr.AudioData(b''.join(frames), tasa_muestreo, sample_width=2)


    try:
        texto = reconocedor.recognize_google(audio_grabado, language='es-ES')
        print("Texto reconocido:")
        print(texto)
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
    except sr.RequestError as e:
        print("Error al solicitar resultados al servicio de reconocimiento de voz de Google: {0}".format(e))

grabar_y_convertir_audio()
