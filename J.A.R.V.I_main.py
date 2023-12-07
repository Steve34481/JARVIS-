import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import datetime
import webbrowser
import os
import tkinter as tk
from tkinter import messagebox
import threading

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak_tts(text):
    tts = gTTS(text=text, lang='en')
    tts.save('jarvis_audio.mp3')
    os.system('start jarvis_audio.mp3')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query.lower()
    except Exception as e:
        print(e)
        print("Couldn't understand the audio. Please try again.")
        return None

def run_jarvis():
    speak("Hello! I am Jarvis. How can I assist you today?")

    while True:
        command = take_command()

        if command:
            if 'time' in command:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")
            elif 'open website' in command:
                speak("Sure. Which website would you like to open?")
                website = take_command()
                if website:
                    webbrowser.open(f"https://www.{website}.com")
            elif 'open notepad' in command:
                os.system("notepad.exe")
            elif 'exit' in command:
                speak("Goodbye!JARVIS")
                break
            else:
                speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    run_jarvis()

class JarvisGUI:
    def __init__(self, master):
        self.master = master
        master.title("Jarvis GUI")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for user input
        self.entry_label = tk.Label(self.master, text="Enter command:")
        self.entry_label.pack(pady=10)

        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack(pady=10)

        # Button to trigger Jarvis actions
        self.submit_button = tk.Button(self.master, text="Submit", command=self.run_jarvis)
        self.submit_button.pack(pady=10)

        # Text widget to display Jarvis responses
        self.response_text = tk.Text(self.master, height=10, width=50)
        self.response_text.pack(pady=10)

        # Scrollbar for the text widget
        scrollbar = tk.Scrollbar(self.master, command=self.response_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.response_text.config(yscrollcommand=scrollbar.set)

        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()

    def speak_tts(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save('jarvis_audio.mp3')
        os.system('start jarvis_audio.mp3')

    def speak_engine(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def take_command(self):
        query = self.entry.get().lower()
        self.response_text.insert(tk.END, f"User: {query}\n")
        return query

    def run_jarvis(self):
        command = self.take_command()

        if command:
            if 'type' in command:
                self.speak_tts("Sure. Please start typing.")
                # Implement typing functionality here
            elif 'time' in command:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                self.speak_tts(f"The current time is {current_time}")
            elif 'open website' in command:
                self.speak_tts("Sure. Which website would you like to open?")
                # Implement website opening functionality here
            elif 'open notepad' in command:
                os.system("notepad.exe")
            elif 'exit' in command:
                self.speak_tts("Goodbye!")
            else:
                self.speak_tts("I'm sorry, I didn't understand that command.")

# Create and run the Tkinter application
root = tk.Tk()
jarvis_app = JarvisGUI(root)
root.mainloop()
    