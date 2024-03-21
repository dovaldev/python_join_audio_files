import argparse
from pydub import AudioSegment
import os


def convertir_a_mp3(ruta_archivo_wav):
    # Carga el archivo WAV
    audio = AudioSegment.from_wav(ruta_archivo_wav)
    # Genera la ruta de salida para el archivo MP3
    ruta_archivo_mp3 = os.path.splitext(ruta_archivo_wav)[0] + ".mp3"
    # Exporta el audio como MP3
    audio.export(ruta_archivo_mp3, format="mp3")
    return ruta_archivo_mp3


def unir_archivos_de_audio(carpeta_audio, archivo_salida):
    # Lista para almacenar los segmentos de audio
    segmentos_audio = []


    # Recorre todos los archivos en la carpeta de audio
    print('Procesando archivos de audio en la carpeta...')
    for archivo in os.listdir(carpeta_audio):
        ruta_absoluta = os.path.join(carpeta_audio, archivo)
        print(f'Procesando archivo: {ruta_absoluta}')
        if archivo.endswith(".wav"):
            # Si es un archivo WAV, lo convierte a MP3
            ruta_mp3 = convertir_a_mp3(ruta_absoluta)
            segmentos_audio.append(AudioSegment.from_mp3(ruta_mp3))
        elif archivo.endswith(".mp3"):
            # Si es un archivo MP3, lo carga directamente
            segmentos_audio.append(AudioSegment.from_mp3(ruta_absoluta))

    # Concatena los segmentos de audio en orden ascendente por filename
    audio_unido = sum(segmentos_audio)

    # Exporta el audio unido a un nuevo archivo mp3
    audio_unido.export(archivo_salida + '.mp3', format="mp3")

    print("Archivos de audio unidos correctamente.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script para unir archivos de audio en una carpeta.')
    parser.add_argument('--folder', dest='carpeta_audio', type=str, required=True,
                        help='La carpeta que contiene los archivos de audio')
    parser.add_argument('--file', dest='archivo_salida', type=str, required=True,
                        help='El nombre del archivo de salida MP3')

    args = parser.parse_args()

    unir_archivos_de_audio(args.carpeta_audio, args.archivo_salida)
