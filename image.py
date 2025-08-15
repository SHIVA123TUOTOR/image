import streamlit as st
import requests

# 🔐 Set your Groq API key
GROQ_API_KEY = "your_groq_api_key"

# 📤 Image generation function
def generate_image(prompt, size="1024x1024"):
    url = "https://api.groq.com/openai/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "stable-diffusion-xl",
        "prompt": prompt,
        "n": 1,
        "size": size
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["data"][0]["url"]
    else:
        st.error("Image generation failed.")
        return None

# 🖼️ Streamlit UI
st.title("🧠 JarvisAI Image Generator (Groq SDXL)")
prompt = st.text_input("Enter your image prompt", "a modular AI assistant in a cyberpunk lab")
size = st.selectbox("Select image size", ["512x512", "768x768", "1024x1024"])

if st.button("Generate Image"):
    with st.spinner("Generating..."):
        image_url = generate_image(prompt, size)
        if image_url:
            st.image(image_url, caption="Generated Image", use_column_width=True)
            st.markdown(f"[Download Image]({image_url})")
