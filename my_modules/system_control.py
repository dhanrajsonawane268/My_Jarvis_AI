import os
from my_modules.voice_output import speak
from .logger import log_event  # ensure logger.py exists

# ✅ Application paths (configure once)
app_paths = {
    "notepad": "notepad.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "calculator": "calc.exe",
    # Add more apps here
}

# ✅ App open/close handler
def handle_app_commands(user_input):
    user_input = user_input.lower()

    for app in app_paths:
        if f"open {app}" in user_input:
            try:
                os.system(f'start {app_paths[app]}')
                speak(f"Opening {app}")
                log_event(f"Opened {app}")
            except Exception as e:
                speak(f"Failed to open {app}")
                log_event(f"Error opening {app}: {e}")
            return True

        elif f"close {app}" in user_input:
            try:
                os.system(f"taskkill /f /im {os.path.basename(app_paths[app])}")
                speak(f"Closing {app}")
                log_event(f"Closed {app}")
            except Exception as e:
                speak(f"Failed to close {app}")
                log_event(f"Error closing {app}: {e}")
            return True

    return False  # No app match found

# ✅ System-level commands: shutdown, restart, sleep
def handle_system_commands(command):
    command = command.lower()

    if "shutdown" in command:
        speak("Shutting down your computer.")
        log_event("System shutdown initiated")
        os.system("shutdown /s /t 1")

    elif "restart" in command:
        speak("Restarting your computer.")
        log_event("System restart initiated")
        os.system("shutdown /r /t 1")

    elif "sleep" in command:
        speak("Putting the system to sleep.")
        log_event("System sleep initiated")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    else:
        log_event("Unknown system command attempted")
        speak("System command not recognized.")
