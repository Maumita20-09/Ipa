from gtts import gTTS
import os

def save_speech(text, filename="speech.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"Audio saved as {filename}. You can download it.")

while True:
    text = input("Enter text to convert to speech (or type 'exit' to quit): ")
    if text.lower() == "exit":
        break
    
    save_speech(text)
    print("To download the file, use the Codespaces file explorer.")