import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)
    except:
        print("Sorry, could not understand")
        return "None"

    return command.lower()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am your voice assistant. How can I help you?")

if __name__ == "__main__":
    wish_user()

    while True:
        command = take_command()

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("The time is " + time)

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            webbrowser.open("https://google.com")

        elif "wikipedia" in command:
            speak("Searching Wikipedia...")
            query = command.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
