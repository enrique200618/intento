
from diffusers import StableDiffusionPipeline
import torch

# Cargar el modelo de Stable Diffusion desde Hugging Face
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4-original", torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # Usa GPU si tienes una

def generate_image_from_text(prompt):
    image = pipe(prompt).images[0]
    image.show()
    return image
