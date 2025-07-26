# my_modules/fun_module.py
import pyjokes
from my_modules.voice_output import speak
import time

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def handle_joke_command(command):
    if "joke" in command:
        speak("Here's a joke for you.")
        while True:
            tell_joke()
            time.sleep(1)  # small pause
            speak("Do you want one more joke? Say yes or no.")
            from my_modules.jarvis_voice import get_voice_input
            response = get_voice_input().lower()
            if "no" in response:
                speak("Okay, no more jokes.")
                break
