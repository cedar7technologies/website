""" This program plays the music and videos from youtube """

import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)
r = sr.Recognizer()
mic = sr.Microphone()

def sayListening(*args):
    message = "Engine is started"
    engine.say(message)
    while True:
        message = "listening"
        engine.say(message)
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                engine.say("you have said "+r.recognize_google(audio))
        except Exception as e:
                engine.say("sorry, we could not identify, please say that again")

from threading import Thread
thread = Thread(target=sayListening)
thread.start()
engine.startLoop()

# import requests
# from pydub import AudioSegment
# from pydub.playback import play
#
#
# mp3file = requests.get("http://www.https://www.bensound.com/royalty-free-music/track/ukulele/")
# with open('./test.mp3','wb') as output:
#   output.write(mp3file.read())
#
# song = AudioSegment.from_mp3("./test.mp3")
# play(song)
