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
import time
import sys

# ✅ Fun module for jokes
from my_modules.fun_module import handle_joke_command

# 🔐 Load environment variables
load_dotenv()
openai_api_key = os.getenv("fiyfh")
weather_api_key = os.getenv("yiik")
gemini_api_key = os.getenv("uvjuyyv")

# 🪵 Logging
logging.basicConfig(
    filename='jarvis_logs.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 🔑 Gemini config
try:
    genai.configure(api_key=gemini_api_key)
    logging.info("Gemini API configured")
except Exception as e:
    logging.error("Gemini config failed", exc_info=True)

# 🎙️ Text-to-speech
engine = pyttsx3.init()
def speak(text):
    print("🤖 Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# 🎧 Voice input
recognizer = sr.Recognizer()
def listen():
    with sr.Microphone() as source:
        speak("Listening...")
        logging.info("Listening...")
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            logging.info(f"Command: {command}")
            return command.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

# 🧠 Match close commands
def is_command_match(user_input, command_list):
    best_match = difflib.get_close_matches(user_input.lower(), command_list, n=1, cutoff=0.6)
    return best_match[0] if best_match else None

# ✅ Typing animation for Gemini replies
def chatgpt_typing_animation(response):
    for char in response:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

# 🤖 Gemini AI
def chat_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        reply = response.text
        speak("Here's what I found:")
        chatgpt_typing_animation(reply)
        speak(reply)
    except Exception as e:
        speak("Something went wrong with Gemini.")
        logging.error("Gemini error", exc_info=True)

# ✅ Personal Identity Handler
def handle_personal_commands(query):
    query = query.lower()

    if "who am i" in query:
        speak("You are Dhanraj Sonawane, a passionate MCA student from Trinity Academy of Engineering, Pune.")
        print("You are Dhanraj Sonawane, a passionate MCA student from Trinity Academy of Engineering, Pune.")
        return True

    elif "tell me my profile" in query or "my introduction" in query:
        profile = (
            "Your name is Dhanraj Sonawane. "
            "You are currently pursuing MCA from Trinity Academy of Engineering, Pune, under Savitribai Phule Pune University. "
            "You are skilled in Web Development, React.js, Java, SQL, and Python. "
            "You are hardworking, self-motivated, and a fast learner. "
            "Your short-term goal is to join a reputed company, and long-term goal is to contribute to the success of an organization like a true professional."
        )
        speak(profile)
        print(profile)
        return True

    return False

# 🧠 Handle all commands
def handle_command(command):
    # ✅ Check personal commands first
    if handle_personal_commands(command):
        return

    match = is_command_match(command, [
        "open notepad", "open chrome", "open youtube",
        "close notepad", "time", "joke", "weather",
        "shutdown", "take a note", "chat with gemini",
        "chatbot", "talk to ai", "ask ai", "gemini chat",
        "ai assistant", "exit", "stop"
    ])

    if match == "open notepad":
        speak("Opening Notepad")
        os.system("start notepad")

    elif match == "open chrome":
        speak("Opening Chrome")
        os.system("start chrome")

    elif match == "open youtube":
        speak("Opening YouTube")
        os.system("start https://youtube.com")

    elif match == "close notepad":
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")

    elif match == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif match == "joke":
        handle_joke_command(command)  # ✅ Infinite loop jokes

    elif match == "weather":
        try:
            city = "Pune"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
            res = requests.get(url).json()
            if res.get("main"):
                temp = res['main']['temp']
                desc = res['weather'][0]['description']
                speak(f"It's {temp}°C with {desc} in {city}.")
            else:
                speak("Sorry, couldn't fetch weather data.")
        except:
            speak("Error while fetching weather.")

    elif "play" in command and "on youtube" in command:
        song = command.replace("play", "").replace("on youtube", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif match == "shutdown":
        speak("Shutting down your computer")
        os.system("shutdown /s /t 1")

    elif match == "take a note":
        speak("What should I write?")
        note = listen()
        if note:
            with open("notes.txt", "a") as f:
                f.write(f"{datetime.datetime.now()}: {note}\n")
            speak("Note saved.")

    elif match in ["chat with gemini", "chatbot", "talk to ai", "ask ai", "gemini chat", "ai assistant"]:
        speak("Sure! What would you like to ask?")
        question = listen()
        if question:
            chat_with_gemini(question)

    elif match in ["exit", "stop"]:
        speak("Goodbye! Jarvis signing off.")
        exit()

    else:
        speak("Sorry, I didn't understand that.")

# 🔁 Main Loop
def listen_and_respond():
    speak("Jarvis is listening. Speak your command.")
    while True:
        query = listen().lower()
        if query:
            print(f"🎤 You said: {query}")
            handle_command(query)
        if 'exit' in query or 'stop' in query:
            speak("Shutting down. Have a great day!")
            break

# 🟢 Entry Point
if __name__ == "__main__":
    speak("Hello Dhanraj, I am your Modern Jarvis. How can I assist you today?")
    logging.info("Jarvis Activated")
    listen_and_respond()
