#------------------------------------TITAN: Tech based Interactive Task & Assistant Network------------------------------------#
# TITAN is a voice assistant that can perform various tasks such as answering questions, providing weather updates, fetching news, etc.#

import speech_recognition as sr
import pyaudio
import pyttsx3
from google import genai
import requests
import spacy

# Initializing TTS engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)     # Adjust voice speed

# Loading NLP model
nlp = spacy.load('en_core_web_sm')

# Gemini API key
client = genai.Client(api_key="AIzaSyAsewzyDvG40BeEpLTpg6eGqDwaJGekyJc")

# News API key
NEWS_API_KEY = "0d00007d9dfc4f9090ca1d859ffaa81b"

# Make bot speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen and convert speech to text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return "I couldn't understand that."
    except sr.RequestError:
        return "There was an error with the recognition service."

# Interact with Gemini AI API
def chat_with_gem(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )
    response_text = response.text
    
    # Remove asterisk(*) if present
    response_text = response_text.replace("*", "").strip()
    return response_text

# Fetch the weather (What is the weather in New York?)
def get_weather(city):
    API_KEY = "793a089de0765dfac4a9712bce6581ac"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("main"):
        temperature = response["main"]["temp"]
        description = response["weather"][0]["description"]
        return f"The temperature in {city} is {temperature}°C with {description}."
    return "Sorry, I couldn't fetch the weather."

#Fetch news
def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()

    if response.get("articles"):
        articles = response["articles"][:5] #Top 5 articles
        news = [f"{article['title']} - {article['source']['name']}" for article in articles]
        return "Here are the top news articles:\n" + "\n".join(news)
    return "Sorry, I couldn't fetch the news."

# Process user commands
def process_command(command):
    doc = nlp(command)

    if "weather" in command:
        for ent in doc.ents:
            if ent.label_=="GPE":
                return get_weather(ent.text)
        return "Which city do you want the weather for?"
    
    elif "news" in command:
        for ent in doc.ents:
            if ent.label_ == "ORG" or ent.label_ == "PERSON" or ent.label_ == "GPE" or ent.label_ == "PRODUCT" or ent.label_ == "EVENT" or ent.label_ == "LAW" or ent.label_ == "NORP":
                return get_news(ent.text)
        return "What topic do you want the news for?"

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    
    else:
        return chat_with_gem(command)

# Main
if __name__ == "__main__":
    speak("Hi I am Titan, your personal assistant. How can I help you today?")
    while True:
        user_input = listen()
        print("You:", user_input)

        if user_input:
            response = process_command(user_input)
            print("Assistant:", response)
            speak(response)