import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os  
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greetme import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break 

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")

                elif "open" in query:
                   from Dictapp import openappweb
                   openappweb(query)
                elif "close" in query:
                   from Dictapp import closeappweb
                   closeappweb(query)

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                   from SearchNow import searchYoutube
                   searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
# temperature function 
                elif "temperature" in query:
                   search = "temperature in delhi"
                   url = f"https://www.google.com/search?q={search}"
                   r  = requests.get(url)
                   data = BeautifulSoup(r.text,"html.parser")
                   temp = data.find("div", class_ = "BNeawe").text
                   speak(f"current{search} is {temp}")
# weather function 
                elif "weather" in query:
                   search = "temperature in delhi"
                   url = f"https://www.google.com/search?q={search}"
                   r  = requests.get(url)
                   data = BeautifulSoup(r.text,"html.parser")
                   temp = data.find("div", class_ = "BNeawe").text
                   speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                   print("input time example:- 10 and 10 and 10")
                   speak("Set the time")
                   a = input("Please tell the time :- ")
                   alarm(a)
                   speak("Done,sir")   
# Time function 
                elif "the time" in query:
                   strTime = datetime.datetime.now().strftime("%H:%M")    
                   speak(f"Sir, the time is {strTime}")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
# finally sleep 
                elif "finally sleep" in query:
                   speak("Going to sleep,sir")
                   exit()
# reminder
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())    
# Calculator  
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
# Whatsapp
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage() 
# Shutdown
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break    
                    for i in range(3):
                        a = input("Enter Password to open Jarvis :- ")
                        pw_file = open("password.txt","r")
                        pw = pw_file.read()
                        pw_file.close()
                        if (a==pw):
                            print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
                            break
                        elif (i==2 and a!=pw):
                            exit()

                        elif (a!=pw):
                            print("Try Again")          
                                
from INTRO import play_gif
play_gif
                
    
