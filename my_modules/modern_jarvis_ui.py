import customtkinter as ctk
from PIL import Image
import pyttsx3
import speech_recognition as sr
import webbrowser
import threading
import os
import datetime
import pywhatkit
import requests
import random
import openai
import difflib
import logging
from dotenv import load_dotenv

# -------------------- Environment Setup --------------------
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") or ""
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY") or ""
CITY_NAME = os.getenv("CITY_NAME") or "Pune"

# -------------------- Logging Setup --------------------
logging.basicConfig(filename="jarvis.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------- Voice Engine Init --------------------
engine = pyttsx3.init()
lock = threading.Lock()

# -------------------- Global UI Vars --------------------
textbox = None
app = None

# -------------------- Voice Functions --------------------
def speak(text):
    with lock:
        logging.info(f"Speak: {text}")
        print("🤖 Jarvis:", text)
        if textbox:
            textbox.insert("end", f"🤖 Jarvis: {text}\n")
            textbox.see("end")
        engine.say(text)
        engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        speak(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, network error.")
        return ""

# -------------------- Command Helpers --------------------
def is_similar_command(command, keywords):
    for word in command.split():
        for keyword in keywords:
            if difflib.SequenceMatcher(None, word, keyword).ratio() > 0.75:
                return True
    return False

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        logging.error(f"OpenAI Error: {e}")
        return "Something went wrong while connecting to GPT."

# -------------------- Command Handling --------------------
def handle_command(command):
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")

    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "close notepad" in command:
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "weather" in command:
        speak("Checking weather...")
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}&units=metric"
            res = requests.get(url).json()
            if res.get("main"):
                temp = res['main']['temp']
                desc = res['weather'][0]['description']
                speak(f"It's {temp}°C with {desc} in {CITY_NAME}.")
            else:
                speak("Sorry, couldn't fetch weather.")
        except Exception as e:
            logging.error(f"Weather error: {e}")
            speak("Weather service is unavailable.")

    elif "joke" in command:
        jokes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "What did the computer do at lunch time? Had a byte.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        speak(random.choice(jokes))

    elif "play" in command and "on youtube" in command:
        song = command.replace("play", "").replace("on youtube", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "shutdown" in command:
        speak("Shutting down system")
        os.system("shutdown /s /t 1")

    elif "design idea" in command or "design" in command:
        ideas = [
            "Try a futuristic dashboard.",
            "Use neumorphism UI.",
            "Make a health tracker app with glassmorphism."
        ]
        speak(random.choice(ideas))

    elif "take a note" in command:
        speak("What should I note?")
        note = listen()
        if note:
            with open("notes.txt", "a") as f:
                f.write(f"{datetime.datetime.now()}: {note}\n")
            speak("Note saved.")

    elif is_similar_command(command, ["chat with gpt", "ask gpt", "chatbot"]):
        speak("What would you like to ask?")
        question = listen()
        if question:
            response = chat_with_gpt(question)
            speak(response)

    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching {query} on Google.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What do you want me to search?")

    elif "stop" in command or "exit" in command:
        speak("Goodbye. Shutting down.")
        app.quit()

    elif command:
        speak("Sorry, I didn't understand that.")

# -------------------- GUI Setup --------------------
def start_listening():
    command = listen()
    if command:
        textbox.insert("end", f"You: {command}\n")
        textbox.see("end")
        handle_command(command)

def launch_gui():
    global app, textbox
    print("🚀 GUI Launching...")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Modern Jarvis - AI Assistant")
    app.geometry("800x500")

    # Header
    title_label = ctk.CTkLabel(app, text="Modern Jarvis AI Assistant", font=ctk.CTkFont(size=24, weight="bold"))
    title_label.pack(pady=20)

    # Output Textbox
    textbox = ctk.CTkTextbox(app, height=250, font=("Consolas", 14))
    textbox.pack(pady=10, padx=20)

    # Button
    ctk.CTkButton(app, text="🎧 Activate Jarvis", command=lambda: threading.Thread(target=start_listening).start()).pack(pady=20)

    # Greeting
    threading.Thread(target=lambda: speak("Hello Dhanraj, I am your upgraded Jarvis. How can I help today?"), daemon=True).start()

    app.mainloop()

# -------------------- Main --------------------
if __name__ == "__main__":
    launch_gui()
