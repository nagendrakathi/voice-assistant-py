import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Library for speech recognition
import datetime  # Module to handle date and time
import wikipedia  # Module to interact with Wikipedia
import webbrowser  # Module to open web browsers
import os  # Module to interact with the operating system
import smtplib  # Module for email sending capabilities
import random  # Module for generating random numbers or selecting random items
import pygame  # Library to handle sound and music
import requests  # Module to handle HTTP requests

# Initialize the pyttsx3 engine for speech synthesis
engine = pyttsx3.init('sapi5')

# Set the voice property to a female voice and adjust the speech rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use index 1 for a female voice
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)  # Set the speech rate to 175 words per minute

# Initialize pygame for playing music
pygame.init()

# Function to make the assistant speak
def speak(audio):   
    engine.say(audio)  # Text-to-speech
    engine.runAndWait()  # Process speech in queue

# Function to play music using pygame
def play_music():
    music_path = "<--# Path to the music file-->"
    pygame.mixer.music.load(music_path)  # Load the music file
    pygame.mixer.music.play()  # Play the music

# Function to wish the user based on the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)  # Get the current hour
    if 0 <= hour < 12:  # Morning greeting
        speak("Good Morning!")    
    elif 12 <= hour < 18:  # Afternoon greeting
        speak("Good Afternoon!")       
    else:  # Evening greeting
        speak("Good Evening!")      

    speak('Hello there. I am Siri, your virtual assistant. How may I help you?')

# Function to listen to the user's voice command
def takeCommand():
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:  # Use the default microphone as input
        print("Listening...")
        r.pause_threshold = 1  # Wait 1 second before considering the speech complete
        audio = r.listen(source)  # Listen to the input
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')  # Recognize speech using Google
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")  # Ask the user to repeat if recognition fails
            return "None"
        return query

# List of jokes or facts
jokes_or_facts = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Did you know that a group of crows is called a murder?",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!"
    # Add more jokes or facts as needed
]

# Function to tell a random joke or fact
def tell_joke_or_fact():
    joke_or_fact = random.choice(jokes_or_facts)  # Randomly select a joke or fact
    speak(joke_or_fact)  # Speak the joke or fact
    print(joke_or_fact)  # Print the joke or fact

# Main function to execute the virtual assistant
if __name__ == "__main__":  # Corrected the name condition
    wishMe()  # Wish the user based on the time of day
    pygame.mixer.init()  # Initialize the mixer for music playback
    flag = True  # Control the loop
    while flag:
        query = takeCommand().lower()  # Get the user's command and convert to lowercase
        
        # Search Wikipedia if the command contains 'wikipedia'
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")  # Remove the 'wikipedia' keyword from the query
            results = wikipedia.summary(query, sentences=5)  # Get a summary of the topic from Wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        # Open YouTube if the command contains 'open youtube'
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        # Open Google if the command contains 'open google'
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        # Open the Times of India if the command contains 'open times of india'
        elif 'open times of india' in query:
            webbrowser.open("timesofindia.indiatimes.com")
        
        # Tell the current time if the command contains 'the time'
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Get the current time
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        
        # Respond to the 'how are you' command
        elif 'how are you' in query:
            speak("I am fine, thank you. How can I help you today")
            print("I am fine, thank you. How can I help you today")
        
        # Tell a joke or fact if the command contains 'joke' or 'fact'
        elif 'joke' in query or 'fact' in query: 
            tell_joke_or_fact()
        
        # Play music if the command contains 'play music'
        elif 'play music' in query:
            speak("Sure! Playing music.")
            play_music()
        
        # Exit the program if the command contains 'exit the program'
        elif 'exit the program' in query:
            speak("Thank you, see you soon.")
            print("Thank you, see you soon.")
            flag = False  # Set flag to False to exit the loop