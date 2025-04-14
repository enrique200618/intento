# Importar las librerías necesarias
import openai
from moviepy.editor import ImageSequenceClip  # Línea 2
import os

# Configuración de OpenAI API (asegúrate de poner tu API key aquí)
openai.api_key = 'tu_api_key'

# Función para generar imágenes (como en tu aplicación de generación de imágenes)
def generar_imagenes(texto):
    respuesta = openai.Image.create(prompt=texto, n=1, size="1024x1024")
    imagen_url = respuesta['data'][0]['url']
    return imagen_url

# Función para crear video a partir de imágenes
def crear_video(imagenes):
    clip = ImageSequenceClip(imagenes, fps=24)
    clip.write_videofile("video_salida.mp4", codec="libx264")

# Lógica para generar imágenes y convertirlas en video
imagenes = []
for i in range(5):
    texto = f"Imagen {i+1} para video"
    url_imagen = generar_imagenes(texto)
    # Aquí deberías descargar la imagen y agregarla a la lista
    imagenes.append(url_imagen)  # Guardar la URL de las imágenes generadas

# Crear el video
crear_video(imagenes)
