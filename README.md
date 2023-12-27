![](https://external-preview.redd.it/i-took-gemini-pro-and-pro-vision-for-a-spin-in-the-google-v0-MYIxTMo-dsWDY1wwNa5M-IW3a5FeUYKtpcbKMtLG4OE.jpg)
# Gemini Vision Invoice Chatbot

## Introduction
Gemini Vision Invoice is a Streamlit-based web application designed to analyze invoice images and answer user queries. It leverages the `gemini-pro-vision` model from Google's generative AI to interpret the content of the invoices.

## App
https://geminivisioninvoice.streamlit.app/

## Installation
To run the Gemini Vision Invoice application, you need to have Python installed on your system. Follow these steps to set up the application:

1. Clone the repository to your local machine.
2. Install the required packages using the command: `pip install -r requirements.txt`.

## Setup
Before starting the application, you need to set up an environment variable for the Google API key:

1. Create a `.env` file in the root directory of the project.
2. Add your Google API key to the `.env` file in the following format: `GOOGLE_API_KEY=your_api_key_here`.

## Running the Application
To start the Streamlit application, navigate to the project directory in your terminal and run the command: `streamlit run app.py`.

## Usage
Upon launching the Gemini Vision Invoice application, follow these steps:

1. Enter your query in the 'Input Prompt' field.
2. Upload an invoice image using the provided file uploader.
3. Click on the 'Tell me about the image' button to submit your query.

The application will then display the analysis and response based on the provided image and query.

## API Key Configuration
Ensure that the `GOOGLE_API_KEY` is correctly set in the `.env` file to authenticate the Google generative AI services.

## Functions Description
- `get_gemini_response`: Connects to the `gemini-pro-vision` model and generates a response based on the input prompt and image.
- `input_image_setup`: Handles the uploaded image and prepares it for analysis.

## Application Flow
1. User inputs a prompt.
2. User uploads an invoice image.
3. The application processes the image and prompt.
4. The response is displayed to the user.

For more information or support, refer to the official documentation or contact the developers.

---

Developed with ❤️ using Streamlit and Google's generative AI.

