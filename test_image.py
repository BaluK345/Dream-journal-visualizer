# test_image.py
from image_gen import generate_image

prompt = "A floating castle above the clouds with dreamlike colors"
output_path = "images/test_dream.png"

result = generate_image(prompt, output_path)
print(f"Image saved to: {result}")

