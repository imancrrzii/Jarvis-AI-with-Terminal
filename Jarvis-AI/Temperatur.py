import speech_recognition
import pyttsx3
import requests
from bs4 import BeautifulSoup


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("[LISTENING...]")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("[RECOGNIZING...]")
        query = r.recognize_google(audio, language='en-us')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("[SAY THAT AGAIN]")
        return "None"
    return query


query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def temp():
    speak("where?")
    miejsce=takeCommand().lower()
    search = (f"Temperature in  {miejsce}")
    url = f"https://www.google.com/search?q= {search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div",class_= "BNeawe").text
    speak(f"The temperatur is {temperature}")

