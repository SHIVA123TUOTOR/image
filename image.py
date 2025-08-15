import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

openai.api_key = "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"

st.title("Image Generator")
prompt = st.text_input("Enter prompt")

if st.button("Generate") and prompt:
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    url = response['data'][0]['url']
    img = Image.open(BytesIO(requests.get(url).content))
    st.image(img)
