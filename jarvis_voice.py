# ✅ Upgraded Modern Jarvis AI 2.0 — Secure APIs, Logging, Gemini, Modular

import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
import os
import logging
import datetime
import pywhatkit
import requests
import random
import difflib
import threading
import google.generativeai as genai
import customtkinter as ctk

# 🔐 Load environment variables from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# 🪵 Logging setup
logging.basicConfig(
    filename='jarvis_logs.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 🔑 Configure Gemini
try:
    genai.configure(api_key=gemini_api_key)
    logging.info("Gemini API configured successfully")
except Exception as e:
    logging.error("Gemini API config failed", exc_info=True)

# 🎙️ Text to Speech
engine = pyttsx3.init()
def speak(text):
    print("🤖 Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# 🎧 Speech Recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        logging.info("Listening for voice input...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            logging.info(f"Recognized command: {command}")
            return command.lower()
        except Exception as e:
            logging.error("Speech recognition failed", exc_info=True)
            speak("Sorry, I didn't catch that.")
            return ""

# 🤖 Gemini Chat
def chat_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        logging.info("Gemini responded to prompt")
        return response.text
    except Exception as e:
        logging.error("Gemini error", exc_info=True)
        return "Something went wrong while connecting to Gemini."

# ✅ Similar Command Match
def is_similar_command(command, keywords):
    for keyword in keywords:
        similarity = difflib.SequenceMatcher(None, command, keyword).ratio()
        if similarity > 0.7:
            return True
    return False

# 🧠 Handle Commands
def handle_command(command):
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")
        logging.info("Notepad opened")

    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")
        logging.info("Chrome opened")

    elif "open youtube" in command:
        speak("Opening YouTube")
        os.system("start https://youtube.com")
        logging.info("YouTube opened")

    elif "close notepad" in command:
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")
        logging.info("Notepad closed")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
        logging.info(f"Reported time: {current_time}")

    elif "joke" in command:
        jokes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the computer go to therapy? It had too many bytes.",
            "My computer told me it needed a break, then froze."
        ]
        joke = random.choice(jokes)
        speak(joke)
        logging.info("Told a joke")

    elif "weather" in command:
        speak("Checking weather...")
        try:
            city = "Pune"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
            res = requests.get(url).json()
            if res.get("main"):
                temp = res['main']['temp']
                desc = res['weather'][0]['description']
                speak(f"It's {temp}°C with {desc} in {city}.")
                logging.info(f"Weather: {temp}°C, {desc} in {city}")
            else:
                speak("Sorry, I couldn't fetch weather data.")
                logging.warning("Weather data not found")
        except Exception as e:
            logging.error("Weather fetch failed", exc_info=True)
            speak("Error while fetching weather.")

    elif "play" in command and "on youtube" in command:
        song = command.replace("play", "").replace("on youtube", "").strip()
        speak(f"Playing {song} on YouTube")
        logging.info(f"Playing YouTube song: {song}")
        pywhatkit.playonyt(song)

    elif "shutdown" in command:
        speak("Shutting down your computer")
        os.system("shutdown /s /t 1")
        logging.info("Shutdown initiated")

    elif "take a note" in command:
        speak("What should I write?")
        note = listen()
        if note:
            with open("notes.txt", "a") as f:
                f.write(f"{datetime.datetime.now()}: {note}\n")
            speak("Note saved successfully.")
            logging.info("Note saved")

    elif is_similar_command(command, [
        "chat with gemini", "chatbot", "talk to ai", "ask ai", "gemini chat", "ai assistant"
    ]):
        speak("Sure! What would you like to ask?")
        question = listen()
        if question:
            response = chat_with_gemini(question)
            speak(response)
            logging.info("Gemini Q&A executed")

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Jarvis signing off.")
        logging.info("Jarvis stopped by user command")
        exit()

    elif command:
        speak("Sorry, I didn't understand that command.")
        logging.warning(f"Unrecognized command: {command}")

# 🎛️ For GUI Start Button
def start_listening():
    command = listen()
    if command:
        handle_command(command)

# 👋 Greeting
if __name__ == "__main__":
    speak("Hello Dhanraj, I am your Modern Jarvis. How can I assist you today?")
    logging.info("Jarvis activated")
    while True:
        start_listening()
