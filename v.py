import speech_recognition as sr
import pyttsx3 as p
import datetime as dt
import webbrowser

recognizer = sr.Recognizer()
engine = p.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I'm unable to understand ")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble understanding your voice.")
        return ""


def perform_task(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")

    elif "time" in command:
        current_time = dt.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = dt.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        speak("What would you like to search for?")
        query = listen()
        if query:
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            speak(f"Here are the search results for {query}")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I'm sorry, I don't understand the command.")

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    
    while True:
        command = listen()
        if command:
            perform_task(command)
