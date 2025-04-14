import openai
from moviepy.editor import ImageSequenceClip
import os
import requests
from PIL import Image
from io import BytesIO

# Configura tu API Key de OpenAI
openai.api_key = 'tu-api-key'

# Función para generar imágenes desde texto con OpenAI
def generate_image_from_text(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img

# Función para crear un video a partir de imágenes generadas
def create_video_from_text(prompt, num_images=10, output_file='output_video.mp4'):
    images = []
    for i in range(num_images):
        img = generate_image_from_text(f"{prompt} {i+1}")
        img_path = f"image_{i}.png"
        img.save(img_path)
        images.append(img_path)

    # Crear el video con las imágenes
    clip = ImageSequenceClip(images, fps=1)  # Puedes ajustar el valor de FPS si es necesario
    clip.write_videofile(output_file, codec="libx264")

    # Eliminar las imágenes después de crear el video
    for img_path in images:
        os.remove(img_path)

# Llamada a la función para crear un video
create_video_from_text("Un paisaje futurista con montañas y un atardecer")

