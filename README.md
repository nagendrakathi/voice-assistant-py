# Voice Assistant Project

## Overview
This mini project is a Python-based virtual voice assistant that can listen to voice commands, respond with actions, and even tell jokes or facts. It uses libraries like `pyttsx3` for text-to-speech, `speech_recognition` for recognizing speech, and `pygame` to play music. The assistant can perform tasks such as searching Wikipedia, opening web pages, telling the time, or playing music, making it a versatile and fun project.
See features now 
## Features
- **Voice Commands:** The assistant listens to voice input and recognizes commands using the Google Speech Recognition API.
- **Text-to-Speech:** It speaks back responses using a female voice generated with `pyttsx3`.
- **Wikipedia Search:** You can ask the assistant to search for any topic on Wikipedia and summarize it for you.
- **Web Browsing:** The assistant can open popular websites like YouTube, Google, and the Times of India in your default web browser.
- **Music Player:** It can play music stored locally on your system.
- **Time Announcements:** It can tell you the current time.
- **Jokes and Facts:** Random jokes or facts are presented when asked for them.

## How I Built This Project
1. **Text-to-Speech**: I used the `pyttsx3` library to convert text into speech. The `sapi5` engine is used for speech synthesis, and I configured the assistant to use a female voice.
   
2. **Speech Recognition**: To capture voice input, I used the `speech_recognition` library with the Google Speech API. The assistant listens to commands via the microphone and processes them accordingly.
   
3. **Wikipedia Integration**: I added Wikipedia search functionality using the `wikipedia` library. The assistant can fetch a summary of any topic and speak it aloud.
   
4. **Web Browser Commands**: The assistant can open popular websites like YouTube, Google, and Times of India using the `webbrowser` library.
   
5. **Music Playback**: To make the assistant play music, I used `pygame` to load and play MP3 files from my local directory.
   
6. **Random Jokes/Facts**: I created a list of jokes and facts, and the assistant can pick a random one using the `random` library.
   
7. **Time Announcements**: Using the `datetime` module, the assistant can tell the current time when prompted.
   
8. **Exit Command**: The assistant listens for an exit command and can terminate the session with a goodbye message.

## Project Files
- `main.py`: The main Python file containing all the logic for the virtual assistant.
- `requirements.txt`: A file listing all the dependencies required to run this project.

## How to Run the Project
1. **Install the required dependencies**: Ensure Python is installed on your system, then run:
   ```bash
   pip install -r requirements.txt
