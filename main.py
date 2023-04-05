import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()

# Set the energy threshold
r.energy_threshold = 300

# Set dynamic energy threshold
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)


engine = pyttsx3.init()




def set_reminder():
    # Your code to set a reminder goes here
    pass

def make_todo_list():
    # Your code to create a to-do list goes here
    pass

def search_web(query):
    # Your code to search the web goes here
    pass

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    # Listen for user input
    with sr.Microphone() as source:
        audio = r.listen(source)
        print("Speak now")
    
    try:
        text = r.recognize_google(audio)
        return text
    except:
         return None



while True:
        
        command = listen()

        if command == None:
             speak("I didn't quite catch that")
             continue
        elif "remind me" in command:
             speak("What Should I remind you about?")
             reminder = listen()
             speak(f"Sure, I'll remind you to {reminder} later.")
    
    
