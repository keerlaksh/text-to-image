# app1.py

import streamlit as st
from gradio_client import Client

def generate_image(prompt):
    """
    Function to generate an image based on a text prompt.
    This will call the Gradio API for Stable Diffusion.
    """
    try:
        # Initialize the Gradio client for Stable Diffusion model
        client = Client("stabilityai/stable-diffusion-3.5-large-turbo")
        
        # Define a default negative prompt
        negative_prompt = ""  # You can change this to a more specific negative prompt if needed
        
        # Call the API with the given prompt and the negative_prompt
        result = client.predict(
            prompt=prompt,
            negative_prompt=negative_prompt,  # Providing the required negative_prompt argument
            width=1024,
            height=1024,
            api_name="/infer"
        )
        return result[0]  # Assuming this returns the image URL
    except Exception as e:
        st.error(f"Error generating image: {e}")
        return None

def run():
    """
    Streamlit function to take user input, generate image, and display it.
    """
    # Streamlit layout
    st.title("Story Part to Image Generator")
    st.markdown("### Enter a part of a story or novel to generate an image!")

    # Input field for story part
    input_text = st.text_area("Enter a part of a story or novel:", "")

    # Button to trigger image generation
    if st.button("Generate Image"):
        if input_text.strip():
            st.info("Generating an image based on the story part...")
            # Call the function to generate image
            image_url = generate_image(input_text)
            if image_url:
                st.image(image_url, caption="Visualized Scene", use_column_width=True)
                st.success("Image generation complete!")
            else:
                st.error("Failed to generate an image.")
        else:
            st.error("Please enter a part of a story to generate the image.")
