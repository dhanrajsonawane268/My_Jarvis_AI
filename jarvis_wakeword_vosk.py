# 📁 File: jarvis_wakeword_vosk.py

import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import subprocess
import pyttsx3

# 🔊 TTS setup
engine = pyttsx3.init()
def speak(text):
    print("🤖 Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ✅ Load Vosk model
model_path = "vosk-model-small-en-in-0.4"
if not os.path.exists(model_path):
    print("❌ Model not found! Download and place it in:", model_path)
    exit(1)

model = vosk.Model(model_path)
samplerate = 16000
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# 🎧 Start Wake Word Listening
with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("🎧 Listening for wake word 'hey jarvis'...")

    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            if "text" in result:
                spoken = result["text"].lower()
                print("🧠 You said:", spoken)

                if "hey jarvis" in spoken:
                    speak("Yes Sir, I am Listening!")
                    subprocess.Popen(["python", "modern_jarvis_ui.py"])
                    break
