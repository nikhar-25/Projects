import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()

engine = pyttsx3.init() #initializing the engine
voices = engine.getProperty("voices") #geting voice property
engine.setProperty('voice', voices[1].id) #changing voice from male to female

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    
def user_commands():
    try:
        with sr.Microphone() as source: #take voice i/p from microphone
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'google' in command:
                command = command.replace('google', '')
                print(command)
    except:
        pass
    return command
    
    
def run_google():
    command = user_commands()
    if 'play' in command: 
        song = command.replace('play', '')
        engine_talk('Playing requested song' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' +time)
    elif 'who is' in command:
        name = command.replace('who is' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('Sorry, I could not catch you properly')
        
while True :       
    run_google()