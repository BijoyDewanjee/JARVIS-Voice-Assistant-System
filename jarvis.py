import speech_recognition as sr
import pyttsx3
import logging 
import os
import datetime
import os
import wikipedia
import webbrowser
import random
import subprocess

#logging configuration
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

# Activating Voice from Our System

engine=pyttsx3.init("sapi5")
engine.setProperty('rate', 170)
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

# This  is speak function

def speak(text):
    """
    This function coverts text to voice

    Args:
        text
    returns:
        voice
    
    
    """
    engine.say(text)
    engine.runAndWait()  # after speak it automatic closed

#speak("Hello My name is Bijoy")


# This function recognize the speech and convert it to text
def takeCommand():
    """This function takes command & recognize

    Returns:
        text as query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source: # Microphone Initialize
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

        ## Now Convert audio to text
        try:
             print("Recognizing....")
             query = r.recognize_google(audio, language='en-in')
             print(f"User said: {query}\n")

        except Exception as e:
             logging.info(e)
             print("Say that again please")
             return "None"
        
        return query
    

def greeting():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir! How are you doing?")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir! How are you doing?")
    else:
        speak("Good Evening sir! How are you doing?")
    

    speak("I am Jarvis. Please tell me how may I help you today?")

greeting()

while True:
    query = takeCommand().lower()
    print(query)
    # speak(query)
    if "your name" in query:
        speak("My name is Jarvis")
        logging.info("User asked for assistant's name.")
    
    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")
        logging.info("User asked for current time.")

    # Small talk

    elif "how are you" in query:
        speak("I am functioning at full capacity sir!")
        logging.info("User asked about assistant's well-being.")

    
    elif "who made you" in query:
        speak("I was created by Bijoy Dewanjee sir, a brilliant mind!")
        logging.info("User asked about assistant's creator.")

    
    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")
        logging.info("User expressed gratitude.")

    
    elif "open google" in query:
        speak("ok sir. please type here what do you want to read")
        webbrowser.open("google.com")
        logging.info("User requested to open Google.")

    # For exit

    elif "exit" in query:
        speak("Thank you for your time sir. Have a great day ahead!")
        logging.info("User exited the program.")
        exit()

    else:
        speak("I am sorry, I can't help you with that.")
        logging.info("User asked for an unsupported command.")


      

        

