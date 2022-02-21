import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 

print("Initializing Max")

MASTER = "vivek"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

# speak function will pronouce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)    

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
         speak("Good Evening" + MASTER)  
    speak("I am max and I'm your virtual assistant. How can I help you?")      

# This function will take command from the microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)


    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n") 
    except Exception as e:
        print("Couldn't recognise can you please say that again")
        query = None     
    return query   

def main():
    # Main program starts here
    speak("Initializing Max...")
    wishMe()
    query = takecommand()

    # Logic for executing tasks per the query
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =40)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open("youtube.com")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        #webbrowser.open("google.com")
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "D:\\song"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'what is the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}") 

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\viveak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
main()        
