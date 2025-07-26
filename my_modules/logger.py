# logger.py (inside my_modules folder)
import datetime

def log_event(message):
    """Logs the message with timestamp"""
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("jarvis_log.txt", "a") as f:
        f.write(f"[{time_stamp}] {message}\n")
