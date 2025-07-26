import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice (0 = Male, 1 = Female)
engine.setProperty('rate', 170)  # Speaking speed
engine.say("Hello Dhanraj! This is your Jarvis voice test.")
engine.runAndWait()
