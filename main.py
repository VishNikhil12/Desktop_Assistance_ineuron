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

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',160)

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


#The function for wish me by using time
def wishMe():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon sir. How are you doing")

    else:
        speak("Good evening sir. How are you doing")
    
    speak("I am JARVIS. Tell me sir how can i help you")




if __name__ == "__main__":
    
    wishMe()
while True:
    query = takeCommand().lower()

    if "wikipedia" in query:
        speak("Searching wikipedia")
        query = query.replace("wikipedia"," ")
        results = wikipedia.summary( query, sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)
        
    elif "youtube" in query:
        speak("Opening Youtube")
        webbrowser.open("youtube.com")
        
    elif "google" in query:
        speak("Opening Google")
        webbrowser.open("google.com")
    
    elif "github" in query:
        speak("Opening Github")
        webbrowser.open("github.com")
    elif "goodbye" in query:
        speak("Ok Sir Iam always there for you bye bye")
        exit()