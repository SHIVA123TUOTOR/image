import streamlit as st
import requests

GROQ_API_KEY = "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"

def generate_image(prompt):
    url = "https://api.groq.com/openai/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }
    res = requests.post(url, headers=headers, json=data)
    return res.json()["data"][0]["url"] if res.ok else None

st.title("Groq Image Generator")
prompt = st.text_input("Prompt", "a futuristic AI assistant")

if st.button("Generate"):
    image_url = generate_image(prompt)
    if image_url:
        st.image(image_url)
    else:
        st.error("Failed to generate image.")
