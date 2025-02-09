# from diffusers import StableDiffusionPipeline
# import torch

# # Load a different Stable Diffusion model
# model_id = "stabilityai/stable-diffusion-2"
# device = "cuda" if torch.cuda.is_available() else "cpu"

# # Initialize the pipeline
# pipe = StableDiffusionPipeline.from_pretrained(model_id)
# pipe = pipe.to(device)

# # Provide your text prompt
# prompt = """GHIBSKY style, cozy mountain cabin covered in snow, with smoke curling from the chimney and a warm, inviting light spilling through the windows"""


# # Generate an image based on the prompt
# image = pipe(prompt).images[0]

# # Save the generated image
# image.save("stable_diffusion_output1.png")

# # Display the generated image (optional)
# image.show()

from diffusers import StableDiffusionPipeline
import torch
import uuid
import os

def generate_image(prompt: str):
    # Load a different Stable Diffusion model
    model_id = "stabilityai/stable-diffusion-2"
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Initialize the pipeline
    pipe = StableDiffusionPipeline.from_pretrained(model_id)
    pipe = pipe.to(device)

    # Generate an image based on the prompt
    image = pipe(prompt).images[0]

    # Create unique filename using uuid
    unique_filename = str(uuid.uuid4()) + ".png"
    save_path = os.path.join("static", "generated", unique_filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save the generated image
    image.save(save_path)

    # Display the generated image (optional)
    image.show()

    return save_path

# Example usage
# prompt_text = """GHIBSKY style, cozy mountain cabin covered in snow, with smoke curling from the chimney and a warm, inviting light spilling through the windows"""
# saved_image_path = generate_image(prompt_text)
# print(f"Image saved to: {saved_image_path}")
