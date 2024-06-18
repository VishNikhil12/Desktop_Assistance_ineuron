import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os


# TAKING VOICE FROM SYSTEM

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
#print(voices[1].id)

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(text):
    """
    This Function Recogize text & returns voice 
    
    """
    engine.say(text)
    engine.runAndWait()
    
    
#speak("Hello iam programmer learning python and my name is zira")

# Speech Recognition Function
def takeCommand():
    """
    This Function Recognize Voice & returns Voice
    
    """
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
  
    try:
           print("Recognize..")
           query = r.recognize_google(audio,language = "hindi-in")
           print(f"User said: {query}\n")
           
           
    except Exception as e:
        print("Say that again please... ")
        return "none"
    
    return query




text = takeCommand()
speak(text)
