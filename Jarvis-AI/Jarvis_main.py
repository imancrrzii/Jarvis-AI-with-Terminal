import speedtest
import pyttsx3
import speech_recognition
import webbrowser
from datetime import datetime
import notifications
from pygame import mixer
from plyer import notification
import time
import pyautogui
import random
from bs4 import BeautifulSoup
import requests
import wikipedia
from pywikihow import search_wikihow
import openai
from apikey import api_data
openai.api_key = api_data
completion = openai.Completion()


def Reply(question):
    prompt = f'Chando: {question}\n Jarvis: '
    response = completion.create(
        prompt=prompt, engine="text-davinci-002", stop=None, temperature= 0.5, max_tokens=200)
    answer = response.choices[0].text.strip()
    return answer


from INTRO import play_gif
play_gif

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i == 2 and a != pw):
        exit()

    elif (a != pw):
        print("Try Again")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)
engine.setProperty('volume', 2.0)


def speak(audio):
    engine.setProperty(
        'voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("[LISTENING...]")
        r.pause_threshold = 3
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 0, 7)

    try:
        print("[RECOGNIZING...]")
        query = r.recognize_google(audio, language='en-us')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("[SAY THAT AGAIN]")
        return "None"
    return query


def there_exists(terms):
    for term in terms:
        if term in query:
            return True


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if there_exists(['wake up', 'alexa']):
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                ans = Reply(query)
                print(ans)
                speak(ans)
                if there_exists(['please wait', 'wait for me' 'go to sleep']):
                    speak("Ok sir , You can me call anytime")
                    break
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif there_exists(['hello', 'hi']):
                    speak("Hello sir, how are you ?")
                elif there_exists(['iam fine', 'i am fine']):
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")

                elif "google search" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif there_exists(['temperature', 'weather']):
                    from Temperatur import temp
                    temp()

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

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

                elif 'remember that' in query:
                    rememberMsg = query.replace("remember that", "")
                    rememberMsg = rememberMsg.replace("virrast", "")
                    speak("You tell me you that" + rememberMsg)
                    remember = open('data.txt', "w")
                    remember.write(rememberMsg)
                    remember.close()

                elif 'what do you remember' in query:
                    remember = open('data.txt', 'r')
                    speak("You tell me that " + remember.read())

                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    # You can choose any number of songs (I have only choosen 3)
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open('https://youtu.be/myh5xtfUG-I')
                    elif b == 2:
                        webbrowser.open('https://youtu.be/9JiW1UrLiBo')
                    elif b == 3:
                        webbrowser.open('https://youtu.be/nnZpgbJQVXw')

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input(
                        "Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                elif "schedule my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("Notify System.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )

                elif "open" in query:  # EASY METHOD
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "internet speed" in query:
                    speak("checking speed...")
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576  # Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ", download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                elif "IPL score" in query:
                    from plyer import notification  # pip install plyer
                    import requests  # pip install requests
                    from bs4 import BeautifulSoup  # pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "html.parser")
                    team1 = soup.find_all(
                        class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(
                        class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(
                        class_="cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(
                        class_="cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title="IPL SCORE :- ",
                        message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout=15
                    )

                elif "game" in query:
                    from game import game_play
                    game_play()

                elif 'screenshot' in query:
                    from Screenshot import screenshot
                    screenshot()

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis", "")
                    query = query.replace("translate", "")
                    translategl(query)
