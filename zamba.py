import pyttsx3
import datetime

#Initialized voices to be used 
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speak function to be used by microsoft voices
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#uses speak function(assistant)
def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Zambo Welcomes You! How may I help you ?")

if __name__=="__main__":   #main function
    wishMe();      #function calling