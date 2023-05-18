import speech_recognition as sr
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
# import yfinance as yf # to fetch financial data
import ssl
from logging.config import listen
import pyttsx3
import certifi
import time
import os # to remove created audio files


engine = pyttsx3.init()

class person:
    name = 'iman'
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

# listen for audio and convert it to text:
def record_audio():
    r = sr.Recognizer() # initialise a recogniser
    with sr.Microphone() as source:
        print('Mendengarkan...')
        r.pause_threshold = 1
        audio = r.listen(source)  # listen for the audio via source
 # microphone as source
    try:
        print('Recognizing Speech...')
        voice_data = r.recognize_google(audio, language="id-ID")  # convert audio to text
        print(f"Katamu: {voice_data.lower()}") # print what user said
    except Exception as e:
        speak(f'maaf bisa ulangi {person_obj.name}, saya kurang mengerti')
        voice_data = "None"# error: recognizer does not understand
    return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang="id")
    engine.setProperty('rate', 140)
 # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'ngomong.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"Kata Elsa: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # 1: greeting
    if there_exists(['hai','halo','hello']):
        greetings = [f"Ada apa {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    elif there_exists(["siapa namamu","siapa kamu","siapa nama kamu"]):
        if person_obj.name:
            speak("saya elsa, asisten pribadi kamu")
        else:
            speak("saya elsa. siapa nama kamu?")

    elif there_exists(["nama saya itu"]):
        person_name = voice_data.split("itu")[-1].strip()
        speak(f"okay, aku akan mengingat nama itu {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    elif there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: time
    elif there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 5: search google
    elif there_exists(["halo google"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Ini yang saya temukan untuk {search_term} di google')

    # 6: search youtube
    elif there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Ini yang saya temukan untuk {search_term} di youtube')

    # 7: get stock price
    
    elif there_exists(["tidur", "keluar sekarang", "keluar"]):
        speak("oke nanti panggil lagi aja ya")
        exit()

    else:
        speak("I am not able to do this !")



time.sleep(1)

person_obj = person()
speak(f'Apa ada yang bisa saya bantu {person_obj.name}')
while(1):
    voice_data = record_audio() # get the voice input
    if respond(record_audio().lower()) == 0:
        break