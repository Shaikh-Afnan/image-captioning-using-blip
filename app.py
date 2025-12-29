"""
AI Image Captioning Web Application

This application uses a pre-trained BLIP (Bootstrapped Language Image Pretraining)
transformer model to generate natural language captions for input images.
The web interface is built using Gradio for quick and interactive deployment.
"""

"""
AI Image Captioning Web Application

This application uses a pre-trained BLIP (Bootstrapped Language Image Pretraining)
transformer model to generate natural language captions for input images.
The web interface is built using Gradio for quick and interactive deployment.
"""

import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# --------------------------------------------------
# Load Pre-trained Processor and Model
# --------------------------------------------------
# AutoProcessor handles image preprocessing and text tokenization
# BLIP model performs vision-to-language generation
processor = AutoProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# --------------------------------------------------
# Image Captioning Function
# --------------------------------------------------
def caption_image(input_image: np.ndarray) -> str:
    """
    Generates a descriptive caption for the given image.

    Parameters:
        input_image (np.ndarray): Input image received from Gradio interface

    Returns:
        str: Generated caption describing the image
    """

    # Convert NumPy array to PIL Image and ensure RGB format
    raw_image = Image.fromarray(input_image).convert("RGB")

    # Prompt to guide the caption generation
    prompt_text = "The image of"

    # Prepare model inputs
    inputs = processor(
        raw_image,
        prompt_text,
        return_tensors="pt"
    )

    # Generate caption tokens
    output = model.generate(
        **inputs,
        max_length=50
    )

    # Decode generated tokens into readable text
    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption

# --------------------------------------------------
# Gradio Web Interface
# --------------------------------------------------
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="AI Image Captioning App",
    description=(
        "Upload an image to generate an AI-powered caption "
        "using a transformer-based vision-language model."
    )
)

# --------------------------------------------------
# Launch Application
# --------------------------------------------------
iface.launch()
