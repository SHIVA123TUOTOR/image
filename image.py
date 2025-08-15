import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

# 🔑 New OpenAI API key
client = openai.OpenAI(
    api_key="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"
)

# 🧠 Streamlit UI
st.set_page_config(page_title="JarvisAI Image Generator", layout="centered")
st.title("🖼️ JarvisAI Image Generator")
prompt = st.text_input("Describe the image you want to generate")

if st.button("Generate Image") and prompt:
    try:
        with st.spinner("Generating image..."):
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
    except Exception as e:
        st.error("⚠️ Image generation failed. Try a different prompt or check your API key.")
