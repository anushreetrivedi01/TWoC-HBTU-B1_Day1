import speech_recognition as sr
from time import ctime
import time
import os
import gtts import gTTs
import pygame
from pygame import mixer




def recordAudio():

r=sr.Recognizer()
with sr.Microphone(device_index=1) as source:
print("say something!")
audio=r.listen(source)


try:
data=r.recognize_google(audio)
print("you said: " +data)
except sr.UnknownValueError :
print("google speech recognition could not understand audio")
except sr.RequestError as e:
print("could not request results from google speech recognition service; {0}.format (e))
return data



time.sleep(0.5)
print("speak now . . .")
recordAudio()
