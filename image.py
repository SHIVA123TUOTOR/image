import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

# 🔑 Your OpenAI API key
client = openai.OpenAI(
    api_key="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"
)

st.title("🖼️ JarvisAI Image Generator")
prompt = st.text_input("Enter your image prompt")

if st.button("Generate Image") and prompt:
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        n=1
    )
    image_url = response.data[0].url
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))
    st.image(image, caption="Generated Image", use_column_width=True)
