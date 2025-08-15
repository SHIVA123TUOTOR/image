import streamlit as st
import openai
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from datetime import datetime

# 🔑 OpenAI API key (use st.secrets for Streamlit Cloud)
client = openai.OpenAI(
    api_key="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"
)

st.title("🖼️ JarvisAI Image Generator")
prompt = st.text_input("Enter your image prompt")

if st.button("Generate Image") and prompt:
    try:
        with st.spinner("Generating image..."):
            response = client.images.generate(
                model="dall-e-2",  # ✅ Use supported model
                prompt=prompt,
                size="1024x1024",
                n=1
            )
            image_url = response.data[0].url
            image_data = requests.get(image_url).content
            image = Image.open(BytesIO(image_data))

            # 🖋️ Add watermark
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            draw.text((10, 10), "JarvisAI", font=font, fill=(255, 255, 255))

            # 💾 Save image locally
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"jarvisai_image_{timestamp}.png"
            image.save(filename)

            # 📤 Display image
            st.image(image, caption="Generated Image", use_column_width=True)
            st.success(f"Saved as {filename}")

    except Exception as e:
        st.error("⚠️ Image generation failed. Try a different prompt or check your API key.")
