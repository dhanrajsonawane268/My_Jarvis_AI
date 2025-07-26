import webbrowser
from my_modules.voice_output import speak

def handle_web_search(command):
    if "google" in command or "search" in command:
        speak("What should I search on Google?")
        query = input("🔍 Type or say your search: ")  # you can also voice-enable this
        url = f"https://www.google.com/search?q={query}"
        speak(f"Searching Google for {query}")
        webbrowser.open(url)
        return True

    elif "youtube" in command or "video" in command:
        speak("What should I play on YouTube?")
        query = input("▶️ Type or say your YouTube search: ")
        url = f"https://www.youtube.com/results?search_query={query}"
        speak(f"Playing {query} on YouTube")
        webbrowser.open(url)
        return True

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        return True

    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
        return True

    return False
