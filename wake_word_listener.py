import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import subprocess

model_path = "vosk_model/vosk_model"  # ✅ path fix (तुझं directory नुसार)
if not os.path.exists(model_path):
    print("❌ Model folder not found at", model_path)
    exit(1)

model = vosk.Model(model_path)
samplerate = 16000
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def wake_word_start():
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🎧 Listening for 'hey jarvis'...")

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if "text" in result:
                    spoken = result["text"]
                    print("🧠 You said:", spoken)
                    if "hey jarvis" in spoken.lower():
                        print("✅ Wake word detected! Launching Jarvis UI...")
                        subprocess.Popen(["python", "modern_jarvis_ui.py"])
                        break

# Direct run support
if __name__ == "__main__":
    wake_word_start()
