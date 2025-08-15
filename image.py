import streamlit as st
import openai
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from datetime import datetime

# 🔑 Hardcoded API key (local use only)
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("🖼️ JarvisAI Image Generator")
prompt = st.text_input("Enter your image prompt")

if st.button("Generate Image") and prompt:
    with st.spinner("Generating..."):
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = response.data[0].url
        image_data = requests.get(image_url).content
        image = Image.open(BytesIO(image_data))

        # 🖋️ Watermark
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((10, 10), "JarvisAI", font=font, fill=(255, 255, 255))

        # 💾 Save image
        filename = f"jarvisai_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        image.save(filename)

        st.image(image, caption="Generated Image", use_column_width=True)
        st.success(f"Saved as {filename}")