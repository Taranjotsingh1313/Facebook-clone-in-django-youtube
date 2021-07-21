import webbrowser
import speech_recognition as s
import pyaudio
import subprocess
import pyttsx3
# webbrowser.open("https://studio.youtube.com/channel/UC2zWqak6KZzKGIr59_pJlUA",new=1)
# subprocess.Popen('C://Users//SIMAR//AppData//Local//Programs//Microsoft VS Code//Code.exe')
sr  = s.Recognizer()
a = pyttsx3.init()

with s.Microphone() as m:
    print("Listening......")
    audio = sr.listen(m)
    if audio:
        query = sr.recognize_google(audio,language='eng-in')
        if query[0] == 'j':

            a.say(query)
            a.runAndWait()
    else:
        print('No')