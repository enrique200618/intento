
import openai
import requests
from PIL import Image
from io import BytesIO

# Configura tu API key de OpenAI
openai.api_key = 'TU_API_KEY'

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
