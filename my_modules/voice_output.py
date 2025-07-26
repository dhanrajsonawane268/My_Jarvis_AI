import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)  # speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female

def speak(text):
    print("🤖 Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
