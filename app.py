import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API (ensure your API key is correctly set in .env)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image_parts, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([prompt, image_parts[0], input_text])
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

if submit:
    try:
        image_data = input_image_setup(uploaded_file)
        input_prompt = """
            You are an expert in understanding images, specifically invoices.
            You will receive input images as invoices &
            you will have to answer questions based on the input image.
            """
        response = get_gemini_response(input_text, image_data, input_prompt)
        st.subheader("The Response is")
        st.write(response)
    except FileNotFoundError as e:
        st.error(str(e))
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
