import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    print("Spandana:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("You said:", command)
    except sr.UnknownValueError:
        talk("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue. Try again later.")
        return ""
    return command

def run_spandana():
    command = take_command()

    if command == "":
        return

    if "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "what's the time" in command or "what is the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time}")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("I couldn't find information about that person.")

    elif "search for" in command:
        query = command.replace("search for", "").strip()
        talk(f"Searching for {query}")
        pywhatkit.search(query)

    elif "joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome")
            os.startfile(chrome_path)
        else:
            talk("Chrome is not installed or path is incorrect.")

    elif "open code" in command or "open vs code" in command:
        talk("Opening Visual Studio Code")
        os.system("code")  # Assumes 'code' is available in PATH

    elif "open downloads" in command:
        downloads_path = os.path.join(os.environ['USERPROFILE'], "Downloads")
        talk("Opening Downloads folder")
        os.startfile(downloads_path)

    elif "exit" in command or "stop" in command:
        talk("Shutting down. See you later.")
        sys.exit()

    else:
        talk("I heard you, but I don’t understand that yet.")

# Initial greeting
talk("Hello. I'm Spandana, your personal voice assistant.")

# Keep listening in a loop
try:
    while True:
        run_spandana()
except KeyboardInterrupt:
    talk("Goodbye. Spandana signing off.")
