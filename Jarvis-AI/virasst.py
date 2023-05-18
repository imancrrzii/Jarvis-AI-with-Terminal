from datetime import datetime
from logging.config import listen
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
from pywikihow import search_wikihow
import wolframalpha
import pywhatkit
from gtts import gTTS
import os
import PyPDF2
import speedtest
from bs4 import BeautifulSoup
import pyautogui
import requests
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from googletrans import Translator
# import pytube
# from pytube import YouTube
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print('voices')
Assistant.setProperty('voices', voices[1].id)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(audio):
    print(" ")
    Assistant.say(audio)
    print(f" {audio}")
    print(" ")
    Assistant.runAndWait()

def terdapat(terms):
    for term in terms:
        if term in query:
            return True


def takeCommand():

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("[LISTENING...]")
        command.pause_threshold = 2
        audio = command.listen(source)

    try:
        print("[RECOGNITION...]")
        query = command.recognize_google(audio, language='en-us')
        print(f"[YOU SAID] : {query}")

    except Exception as Error:
        return "none"

    return query.lower()


def TaskExe():

    def Music():
        speak("Tell me the name")
        musicName = takeCommand()

        if 'mantap' in musicName:
            os.startfile('D:\\songs\\mantap.mp3')

        else:
            pywhatkit.playonyt(musicName)

        speak("has benn started, Enjoy!")

    # def Whatsapp():
    #     speak("tell me the name")
    #     name = takeCommand()

    #     if 'gblok' in name:
    #         speak("tell me the message")
    #         msg = takeCommand()
    #         speak("tell me the time sir")
    #         speak("time in hour")
    #         hour = int(takeCommand())
    #         speak("time in minutes")
    #         min = int(takeCommand())
    #         pywhatkit.sendwhatmsg("+622175718680", msg, hour, min, 20)
    #         speak("ok sir")

    #     elif 'emak' in name:
    #         speak("tell me the message")
    #         msg = takeCommand()
    #         speak("tell me the time sir")
    #         speak("time in hour")
    #         hour = int(takeCommand())
    #         speak("time in minutes")
    #         min = int(takeCommand())
    #         pywhatkit.sendwhatmsg("+622175718680", msg, hour, min, 20)
    #         speak("ok sir")

    #     else:
    #         speak("tell me the phone number")
    #         phone = int(takeCommand())
    #         ph = '+62' + phone
    #         speak("tell me the message")
    #         msg = takeCommand()
    #         speak("tell me the time sir")
    #         speak("time in hour")
    #         hour = int(takeCommand())
    #         speak("time in minutes")
    #         min = int(takeCommand())
    #         pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
    #         speak("ok sir")

    def openApp():
        speak("ok sir, wait a second")
        if 'figma' in query:
            os.startfile(r"C:\Users\User\AppData\Local\Figma\app-116.6.3\Figma.exe")
        elif 'sublime' in query:
            os.startfile("C:\Program Files\Sublime Text 3\sublime_text.exe")
        elif 'chrome' in query:
            os.startfile(
                "C:\Program Files\Google\Chrome\Application\chrome.exe")
        elif 'facebook' in query:
            webbrowser.get('chrome').open('https://www.facebook.com/')
        elif 'instagram' in query:
            webbrowser.get('chrome').open('https://www.instagram.com/')
        elif 'maps' in query:
            webbrowser.get('chrome').open(
                'https://www.google.com/maps/@-2.965504,104.7396352,13z')
        elif 'youtube' in query:
            webbrowser.get('chrome').open('https://www.youtube.com/')

        speak("Your Command succesfully completed")

    def speedTest():
        import speedtest
        speak("checking speed...")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload = int(uploading/800000)

        if 'uploading' in query:
            speak(f"The Uploading speed is{correctUpload} mbp s")
        elif 'downloading' in query:
            speak(f"the downloading speed is{correctDown} mbp s")
        else:
            speak(f"The Downloading is {correctDown} and The Uploading is {correctUpload} mbp s")


    def Dict():
        speak("activated dictionary")
        speak("tell me the problem")
        probl = takeCommand()

        if 'meaning' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("virrast", "")
            # probl = probl.replace("of")
            probl = probl.replace("meaning", "")
            result = Diction.meaning(probl)
            speak(f"the meaning for {probl} is {result}")

        elif 'synonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("virrast", "")
            # probl = probl.replace("of")
            probl = probl.replace("synonym", "")
            result = Diction.synonym(probl)
            speak(f"the Synonim for {probl} is {result}")

        elif 'antonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("virrast", "")
            # probl = probl.replace("of")
            probl = probl.replace("antonym", "")
            result = Diction.antonym(probl)
            speak(f"the Antonym for {probl} is {result}")

        speak("Exited Dictionary")





    def closeApp():
        speak("ok sir, wait a second")

        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'chrome' in query:
            os.startfile("TASKKILL /F /im chrome.exe")

        elif 'figma' in query:
            os.startfile("TASKKILL /F /im Figma.exe")

        elif 'sublime' in query:
            os.startfile("TASKKILL /F /im sublime_text.exe")

        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")

        speak("Succesfully completed")
    
    def temp():
        speak("where?")
        miejsce=takeCommand().lower()
        search = (f"Temperature in  {miejsce}")
        url = f"https://www.google.com/search?q= {search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div",class_= "BNeawe").text
        speak(f"The temperatur is {temperature}")

    def reader():
        speak("tell me the name of book")

        name = takeCommand()

        if 'indonesia' in name:
            os.startfile('D:\Semester 2\Ebook\Robotika Teori dan Aplikasi by Wisnu Jatmiko, Petrus Mursanto, M Iqbal Tawakal, M Sakti Alvissalim, Abdullah Hafidh, Enrico Budianto, M Nanda Kurniawan, Kharda Ahfa, Ken Danniswara, M Anwar Ma’sum, In (z-lib.org).pdf')
            book = open('D:\Semester 2\Ebook\Robotika Teori dan Aplikasi by Wisnu Jatmiko, Petrus Mursanto, M Iqbal Tawakal, M Sakti Alvissalim, Abdullah Hafidh, Enrico Budianto, M Nanda Kurniawan, Kharda Ahfa, Ken Danniswara, M Anwar Ma’sum, In (z-lib.org).pdf', 'rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            speak(f"Number page {pages}")
            speak("from which page ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            speak("in which language?")
            lang = takeCommand()

            if 'indo' in lang:
                trans1 = Translator()
                textIdn = trans1.translate(text, 'in')
                textm = textIdn.text
                speech = gTTS(text = textm)
                try:
                    speech.save('ngomong.mp3')
                    playsound('ngomong.mp3')
                except:
                    playsound('ngomong.mp3')

            else:
                speak(text)
                





    def youtubeAuto():
        speak("whats your command")
        comm = takeCommand()
        if 'pause' in comm:
            keyboard.press('space bar')
        
        elif 'restart' in comm:
            keyboard.press('0')
        elif 'mute' in comm:
            keyboard.press('m')
        elif 'skip' in comm:
            keyboard.press('1')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'film mode' in comm:
            keyboard.press('t')
        
        speak("done")

    def takeIndo():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing...")
                query = command.recognize_google(audio, language='id-ID')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

    def Tran():
        speak("tell me the line")
        line = takeIndo()
        translate = Translator()
        result = translate.translate(line)
        text = result.text
        speak(f"The translation is {text}")

        
    def chromeAuto():
        speak('Chrome Automation started')

        command = takeCommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')
        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

    def screenshot():
        speak("ok boss, what should i name this file")
        path = takeCommand().lower()
        path1name = path + ".png"
        path1 = "D:\\" + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("D:\\")
        speak("here is your")


    while True:
            query = takeCommand()

            if terdapat(['hai','halo','hello']):
                greetings = [f"Ada apa {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
                greet = greetings[random.randint(0,len(greetings)-1)]
                speak(greet)

            # if 'hello' in query:
            #     speak("hello sir, I am Jarvis .")
            #     speak("Your Personal AI Assistant!")
            #     speak("What do you want?")

            elif terdapat(['apa kabar', 'kabar']):
                speak("I am fine sir!")
                speak("Whats About you?")

            elif 'you need a break' in query:
                speak("OK Sir, You can call me Anytime !")
                break

            elif 'bye' in query:
                speak("Ok sir, Bye!")
                break

            elif 'youtube search' in query:
                speak("ok sir, this is what i found for your search")
                query = query.replace("virrast", "")
                query = query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.get('chrome').open(web)
                speak("Done Sir!")

            elif 'google search' in query:
                speak("This is what i found for your search")
                query = query.replace("virrast", "")
                query = query.replace("google search", "")
                pywhatkit.search(query)
                speak("Done sir")

            elif 'website' in query:
                speak("ok sir, launching...")
                query = query.replace("virrast", "")
                query = query.replace("website", "")
                query = query.replace(" ", "")
                web1 = query.replace("open", "")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.get('chrome').open(web2)
                speak("Launched")

            elif 'launch' in query:
                speak("Tell me the name of the website!")
                name = takeCommand()
                web = 'https://www.' + name + '.com'
                webbrowser.get('chrome').open(web)
                speak("Done sir!")

            elif 'facebook' in query:
                speak("ok sir!")
                webbrowser.get('chrome').open("https://www.facebook.com")
                speak("Done sir")

            elif 'music' in query:
                Music()

            elif 'wikipedia' in query:
                speak("searching wikipedia")
                query = query.replace("virrast", "")
                query = query.replace("wikipedia", "")
                wiki = wikipedia.summary(query, 2)
                speak(f"according to wikipedia : {wiki}")

            elif 'whatsapp message' in query:
                Whatsapp()

            elif 'screenshot' in query:
               screenshot()

            elif 'open facebook' in query:
                openApp()

            elif 'open instagram' in query:
                openApp()

            elif 'open figma' in query:
                openApp()

            elif 'open maps' in query:
                openApp()

            elif 'open youtube' in query:
                openApp()

            elif 'open chrome' in query:
                openApp()

            elif 'open sublime' in query:
                openApp()

            elif 'close chrome' in query:
                closeApp()
            elif 'close facebook' in query:
                closeApp()
            elif 'close instagram' in query:
                closeApp()
            elif 'close figma' in query:
                closeApp()
            elif 'close maps' in query:
                closeApp()
            elif 'close youtube' in query:
                closeApp()
            elif 'close sublime' in query:
                closeApp()

            elif 'pause' in query:
                keyboard.press('k')
        
            elif 'restart' in query:
                keyboard.press('0')
            elif 'mute' in query:
                keyboard.press('m')
            elif 'skip' in query:
                keyboard.press('1')
            elif 'back' in query:
                keyboard.press('j')
            elif 'full screen' in query:
                keyboard.press('f')
            elif 'film mode' in query:
                keyboard.press('t')

            elif 'youtube tool' in query:
                youtubeAuto()

            elif 'close new tab' in query:
                keyboard.press_and_release('ctrl + w')
            elif 'open new tab' in query:
                keyboard.press_and_release('ctrl + t')
            elif 'open new window' in query:
                keyboard.press_and_release('ctrl + n')
            elif 'history' in query:
                keyboard.press_and_release('ctrl + h')
            elif 'chrome automation' in query:
                chromeAuto()

            elif 'joke' in query:
                get = pyjokes.get_joke()
                speak(get)
            
            elif 'repeat my word' in query:
                speak("speak sir!")
                jj = takeCommand()
                speak(f"You said : {query}")

            elif 'my location' in query:
                speak("ok sir")
                webbrowser.get('chrome').open('https://www.google.co.id/maps/')

            elif 'dictionary' in query:
                Dict()

            elif 'translator' in query:
                Tran()

            elif 'remember that' in query:
                rememberMsg = query.replace("remember that", "")
                rememberMsg = rememberMsg.replace("virrast", "")
                speak("You tell me you that" +rememberMsg)
                remember = open('data.txt', "w")
                remember.write(rememberMsg)
                remember.close()

            elif 'what do you remember' in query:
                remember = open('data.txt','r')
                speak("You tell me that " +remember.read())

            elif 'google find' in query:
                import wikipedia as googleScrap
                query = query.replace("Jarvis", "")
                query = query.replace("google find", "")
                query = query.replace('google', "")
                speak("this is what i found on the web")
                pywhatkit.search(query)

                try:
                    result = googleScrap.summary(query,3)
                    speak(result)

                except:
                    speak("No speaker")

            elif 'temperatur' in query:
                temp()

            # elif 'book reader' in query:
            #     reader()

            elif 'downloading speed' in query:
                speedTest()

            elif 'uploading speed' in query:
                speedTest()

            elif 'internet speed' in query:
                speedTest()

            elif 'how to' in query:
                speak("Getting data from the internet !")
                op = query.replace("Jarvis", "")
                max_result = 1
                how_to_func = search_wikihow(op, max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

            


        
            # elif 'video downloader' in query:
            #     root = Tk()
            #     root.geometry('500x300')
            #     root.resizable(0,0)
            #     root.title("Youtube Video Downloader")
            #     speak("enter video url her+e")

            #     Label(root, text = "Youtube Video Downloader" ,font = 'cambria 12').pack()
            #     link = StringVar()
            #     Label(root, text = "paste Link Here", font = 'cambria 12').place(x=160, y=60)
            #     Entry(root, width = 70, textvariable = link).place(x=32, y=90)

            #     def videoDownloader():
            #         link = StringVar()
            #         url = YouTube(str(link.get()))
            #         video = url.streams.get_highest_resolution()
            #         video.download()
            #         Label(root, text = "downloaded", font = 'cambria 12').place(x = 180, y=120)
            #         # url = YouTube(str(link.get()))
            #         # video = url.streams.first()
            #         # video.download()
            #         # Label(root, text = "downloaded", font = 'cambria 12').place(x = 180, y=120)

            #     Button(root, text = "Download", font='cambria 12', bg = 'red', padx = 2, command = videoDownloader).place(x=180, y=150)

            #     root.mainloop()
            #     speak("video downloaded")


TaskExe()




