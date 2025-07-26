# 🤖 MY_JARVIS_AI – Your Personal Modern Desktop AI Assistant

Welcome to **MY_JARVIS_AI**, a fully functional, voice-controlled smart assistant inspired by Jarvis from Iron Man. Built using **Python**, this AI can perform various tasks like controlling apps, searching the web, telling jokes, reporting the weather, chatting with AI (ChatGPT), and much more — all via a modern **GUI interface**.

---

## 🧠 Features

- 🎤 **Voice Recognition** using Vosk
- 🧠 **AI ChatBot** powered by OpenAI GPT
- 🖥️ **GUI Interface** with `CustomTkinter`
- 🌐 **Web Search** with smart parsing
- 📅 Time, Date & System Info Reporting
- 😄 **Joke Generator** for entertainment
- 🌦️ **Live Weather Reports** using API
- 📁 File Operations & Notes
- 🔊 Text to Speech using `pyttsx3`
- 🚀 Launch Desktop Apps (Notepad, Chrome, etc.)
- 🔐 Wake-word Detection (`Hey Jarvis`)
- 📄 Logging System for tracking events

---

## 🗂️ Folder Structure

```bash
MY_JARVIS_AI/
├── assets/
│   └── icons/
│       ├── logo.png
│       └── robot_icon.png
├── logs/
│   └── jarvis_log.txt
├── my_modules/
│   ├── __init__.py
│   ├── ai_chat.py
│   ├── fun_module.py
│   ├── jarvis_voice.py
│   ├── logger.py
│   ├── system_control.py
│   ├── voice_input.py
│   ├── voice_output.py
│   ├── web_search.py
│   └── wake_word_listener.py
├── vosk_model/ *(Contains Vosk Indian English model)*
├── main.py
├── modern_jarvis_ui.py
├── jarvis_wakeword_engine.py
├── test_speak.py
├── .gitignore
└── README.md


🛠️ Technologies Used
Language: Python 3.11+

GUI Framework: CustomTkinter

Voice Recognition: Vosk + SpeechRecognition

Text-to-Speech: pyttsx3

AI Chatbot: OpenAI GPT-3.5 Turbo API

APIs: OpenWeatherMap for weather, pyjokes, etc.

🚀 How to Run
1️⃣ Clone the Repo
bash
Copy
Edit
git clone https://github.com/dhanrajsonawane268/My_Jarvis_AI.git
cd My_Jarvis_AI
2️⃣ Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Add Vosk Model
Download the Indian English model vosk-model-small-en-in-0.4
Extract it into the /vosk_model folder.

4️⃣ Add your OpenAI API Key
Create a .env file or directly insert your key in ai_chat.py.

5️⃣ Run the App
bash
Copy
Edit
python main.py
🎯 Future Improvements
Add face recognition for authentication

Email & WhatsApp automation

Local database for knowledge retention

Mobile app version (Kivy / Flutter)

🤝 Contribution
Pull requests are welcome! If you find bugs or want to enhance the assistant, feel free to contribute.

📜 License
This project is licensed under the MIT License.

👤 Author
Dhanraj Rajendra Sonawane
🎓 MCA Student | 💻 Python Developer | 🎙️ AI Enthusiast
🔗 LinkedIn | 📧 dhanrajsonawane268@gmail.com


