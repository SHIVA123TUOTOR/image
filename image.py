import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

openai.api_key = "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"

st.title("🖼️ JarvisAI Image Generator")
prompt = st.text_input("Describe the image you want to generate")

if st.button("Generate Image") and prompt:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": f"Generate an image of: {prompt}"}
                ]}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        image_url = response["choices"][0]["message"]["content"]["parts"][0]["image_url"]
        image_data = requests.get(image_url).content
        image = Image.open(BytesIO(image_data))
        st.image(image, caption="Generated Image", use_column_width=True)

    except Exception as e:
        st.error("⚠️ Image generation failed. Try a simpler prompt or check your API key.")
