import speech_recognition as sr
from gtts import gTTS
import requests
import os

API_KEY = 'AIzaSyDAv1grZi31BJySRMZcc0KtuU1w1-6x-o4'
CSE_ID = '54533f84d132a4bbc'

def search_google(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CSE_ID}"
    response = requests.get(url)
    data = response.json()
    if 'items' in data:
        result = data['items'][0]['snippet']
        return result
    else:
        return "No results found."

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

def listen_and_search():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            search_result = search_google(query)
            print("Search Result:", search_result)
            speak(search_result)
        except sr.UnknownValueError:
            print("Could not understand the audio")
            speak("I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("There was an error in making the request.")

listen_and_search()
