import speech_recognition as sr 
import pyttsx3

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Listening......")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'roko' in command:
        
            print(command)
except:
    pass
    