import streamlit as st
import openai
from moviepy.editor import ImageSequenceClip
import os
from PIL import Image
import shutil

# Configura tu clave de API
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Creador de video desde texto con IA")

texto = st.text_input("Describe la escena que deseas animar (ejemplo: 'una ciudad futurista al atardecer')")

if st.button("Generar imágenes"):
    if texto:
        if os.path.exists("imagenes"):
            shutil.rmtree("imagenes")
        os.makedirs("imagenes", exist_ok=True)

        st.write("Generando imágenes con IA...")

        for i in range(5):
            prompt = f"{texto}, frame {i+1}"
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            image = Image.open(requests.get(image_url, stream=True).raw)
            image.save(f"imagenes/imagen_{i+1}.png")
        
        st.success("Imágenes generadas correctamente.")

        st.write("Creando video...")

        images = [f"imagenes/imagen_{i+1}.png" for i in range(5)]
        clip = ImageSequenceClip(images, fps=1)
        clip.write_videofile("video.mp4")

        st.video("video.mp4")
    else:
        st.warning("Escribe un texto antes de generar imágenes.")
