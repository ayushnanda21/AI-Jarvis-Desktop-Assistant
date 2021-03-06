import pyttsx3
import datetime #for wish me
import speech_recognition as sr #for taking input from user
import wikipedia
import webbrowser
import os
import smtplib

#Initialized voices to be used 
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speak function to be used by microsoft voices
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    '''uses speak function to greet user(assistant)'''
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Zambo Welcomes You! How may I help you ?")

def askCommand():
    '''using microphone to ask user for input'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")

        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")

    except Exception as e:
       #print(e)

        print("I couldn't understand. Please repeat..")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


    

if __name__=="__main__":   #main function
    wishMe();      #function calling
    while True:
        query = askCommand().lower()


#tasks logic
        if 'wikipedia' in query:   #surfing wikipedia conditions
            speak('Searching...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:      
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open linkdin' in query:
            webbrowser.open("linkdin.com")

        elif 'play music' in query:       #music condition
            music_dir ='F:\\Songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open visual code studio' in query:
            codePath ="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email to ayush' in query:
            try:
                speak("What you want to send?")
                content =askCommand()
                to ="xyz@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir.")
            except Exception as e:
                print(e)
                speak("Apologies! Not able to send your email.")