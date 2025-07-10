# image_gen.py

import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os

# 🔁 Load the Stable Diffusion model once at the start
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")  # ✅ Move model to GPU

def generate_image(prompt, output_path):
    """
    Generate an image from a text prompt and save it locally.

    Parameters:
    - prompt (str): The dream description (text input)
    - output_path (str): File path to save the generated image

    Returns:
    - str: Path where the image was saved
    """
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 🔮 Generate image from prompt
    image = pipe(prompt).images[0]

    # 💾 Save image
    image.save(output_path)

    return output_path
