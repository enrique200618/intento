
import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO
from moviepy.editor import ImageSequenceClip
import os

# Configura tu API key de OpenAI
openai.api_key = 'TU_API_KEY'

# Función para generar imágenes con DALL·E 2
def generate_image_from_text(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    img_response = requests.get(image_url)
    img = Image.open(BytesIO(img_response.content))
    return img

# Función para convertir las imágenes en video
def generate_video_from_images(images, fps=24):
    clip = ImageSequenceClip(images, fps=fps)
    video_path = "output_video.mp4"
    clip.write_videofile(video_path, codec="libx264")
    return video_path

# Streamlit App
st.title("Generación de Imágenes a Video desde Texto")

prompt = st.text_input("Escribe una descripción de la escena para generar las imágenes:")
if prompt:
    st.write("Generando imágenes...")
    images = []
    for i in range(5):  # Generamos 5 imágenes
        img = generate_image_from_text(prompt)
        images.append(img)

    st.image(images, caption=[f"Imagen {i+1}" for i in range(len(images))], width=300)

    if st.button("Generar Video"):
        st.write("Generando video...")
        video_path = generate_video_from_images(images)
        st.video(video_path)
