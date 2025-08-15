import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

# ✅ Use the new client-based API
client = openai.OpenAI(
    api_key="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"
)

st.title("🖼️ Simple Image Generator")
prompt = st.text_input("Enter your prompt")

if st.button("Generate") and prompt:
    try:
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size="512x512",
            n=1
        )
        url = response.data[0].url
        img = Image.open(BytesIO(requests.get(url).content))
        st.image(img)
    except Exception as e:
        st.error("Image generation failed. Try a different prompt or check your key.")
