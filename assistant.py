from google import generativeai as genai
import speech_recognition as sr
import pyttsx3
import webbrowser
from apikey import api_data

genai.configure(api_key=api_data)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def Reply(question):
    try:
        response = model.generate_content(question)
        return response.text.strip()
    except Exception:
        return "Sorry, I couldn't generate a response."

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception:
        print("Could not understand. Try again.")
        return "none"
    return query

if __name__ == "__main__":
    speak("Hello, how can I help you?")
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue

        if "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
            continue

        if "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
            continue

        if "bye" in query or "exit" in query:
            speak("Goodbye!")
            break

        answer = Reply(query)
        print(f"AI: {answer}")
        speak(answer)
