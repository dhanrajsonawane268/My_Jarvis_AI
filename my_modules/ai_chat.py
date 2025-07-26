import google.generativeai as genai
import os
from dotenv import load_dotenv
from my_modules.logger import log_event
from my_modules.voice_output import speak

# Load the Gemini API Key from .env
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyD46qPSyX-ScbikbuHIqNyVCWJkUUCov-k"))

def chat_with_gpt(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        if hasattr(response, 'text'):
            return response.text
        else:
            return "Gemini did not return any response."
    except Exception as e:
        log_event("Gemini API Error", str(e))
        return "Gemini chatbot failed to respond."
