import pyttsx3
import speech_recognition as sr
import random
import pyautogui
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def screenshot():
        speak("ok boss, what should i name this file")
        path = takeCommand().lower()
        path1name = path + ".png"
        path1 = "D:\\" + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("D:\\")
        speak("here is your")