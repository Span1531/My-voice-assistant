Spandana – Voice Desktop Assistant

Spandana is a simple Python-based voice assistant that listens to your commands and responds in real time. It can play music, tell the time, search the web, fetch information from Wikipedia, tell jokes, and even open applications on your system.

This project was built to explore speech recognition, text-to-speech systems, and automation using Python.

✨ Features

🎵 Play songs directly on YouTube

🕒 Tell the current time

🌍 Search the web

📚 Fetch short summaries from Wikipedia

😂 Tell random jokes

🖥️ Open applications like:

Google Chrome

Visual Studio Code

Downloads folder

🛑 Voice command to exit the assistant

🎤 Continuous listening until stopped

🛠️ Technologies Used

Python

speech_recognition – For capturing voice input

pyttsx3 – For text-to-speech conversion

pywhatkit – For playing YouTube videos and searching

wikipedia – For fetching summaries

pyjokes – For random jokes

Built-in modules like datetime, os, and sys


⚙️ How It Works

The assistant listens using your system microphone.

It converts your speech into text using Google Speech Recognition.

Based on keywords in your command, it performs the requested task.

It responds back using a female voice engine.

The assistant keeps running in a loop until you say “exit” or “stop”.


📦 Installation

Make sure you have Python installed (Python 3.8+ recommended).

Install the required libraries:

pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes pyaudio

Note: If pyaudio gives an error on Windows, install the compatible wheel file manually.


▶️ How to Run
python assistant.py

Once started, Spandana will greet you and begin listening.

Try commands like:

“Play Believer”

“What is the time?”

“Who is Elon Musk?”

“Search for machine learning”

“Tell me a joke”

“Open Chrome”

“Exit”

💡 Future Improvements

Add weather updates

Add system control (shutdown, restart)

Add custom wake word

Improve natural language understanding

Add GUI interface

📌 Project Purpose

This project was created as a learning experience to understand:

Voice recognition systems

Speech synthesis

Python automation

Real-time interaction handling

It’s a foundational step toward building more advanced AI-powered assistants.

👩‍💻 Author

Developed with curiosity and creativity.
