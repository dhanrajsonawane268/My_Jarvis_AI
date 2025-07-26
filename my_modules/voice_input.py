import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Say something...")
        audio = r.listen(source)

    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("😕 Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("⚠️ Could not request results; check your internet connection.")
        return ""
