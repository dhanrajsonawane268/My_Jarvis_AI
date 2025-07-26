from my_modules.voice_input import listen
from my_modules.voice_output import speak
from my_modules.jarvis_voice import listen_and_respond
from my_modules.system_control import handle_system_commands
from my_modules.web_search import handle_web_search
from my_modules.modern_jarvis_ui import launch_gui

def main():
    speak("Hello Dhanraj, I am online. How can I help you?")
    launch_gui()  # ✅ GUI launch इथे कॉल केलं

if __name__ == "__main__":
    main()
