import streamlit as st
import requests

EDENAI_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTkwMmJiOTMtZTg1Ni00MGIxLWE1ODgtMTFhYjZmMWE4YTQzIiwidHlwZSI6ImFwaV90b2tlbiJ9.JLLMzjD1KHpm0tjzZ26Y2GEH6YlhXgOSbvG4nB18qDg"

def generate_image(prompt):
    url = "https://api.edenai.run/v2/image/generation"
    headers = {
        "Authorization": f"Bearer {EDENAI_API_KEY}"
    }
    payload = {
        "providers": "openai",  # You can also try "stabilityai", "replicate", etc.
        "text": prompt,
        "resolution": "1024x1024",
        "num_images": 1
    }

    res = requests.post(url, headers=headers, json=payload)
    if res.ok:
        image_url = res.json()["openai"]["items"][0]["image"]
        return image_url
    else:
        return None

st.title("EdenAI Image Generator")
prompt = st.text_input("Prompt", "a futuristic AI assistant")

if st.button("Generate"):
    image_url = generate_image(prompt)
    if image_url:
        st.image(image_url)
    else:
        st.error("Image generation failed.")
