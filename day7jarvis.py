import webbrowser as wb
import speech recognition as sr
from tkinter import*
from time import ctime
import time
import os
from gtts import gTTs
import pygame
from pygame import mixer

def speak(audioString):
global x
b=audioString
if len(b) == 0:
return
tts = gTTs(test=b, lang='en-us)
tts.save("voice%s.mp3"%(x))
pygame.init()
pygame.display.set_mode((2,1))
mixer.music.load("voice%s.mp3"%(x))
mixer.music.play(0)




x+=1
clock= pygame.time.clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
pygame.event.poll()
clock.tick(10)



def recordAudio():
r=sr.Recognizer()
with sr.Microphone() as source:
print("Speak...")
audio=r.listen(source)
print("heard...")


data="


ty:

data = r.recognize_google(audio)
print("you said : " + data)
except sr.UnknownValueError:
print("google search recognition could not understand audio")
except sr.RequestError as e:
print("could not request results from googlr speech recognition service;  {0}".format(e))
return data

def jarvis(data):
if "how are you" in data:
speak("i am fine")

elif "what time is it" in data:
speak(ctime())

elif "where is" in data:
data=data.split(" ")
location=data[2]
speak("hold on anushree,I will show you where " + location + "is.")
wb.open_new_tab(https://www.google.n1/maps/place/" +location + "/&amp;")
else :
speak(",,,,,,,I did not get what you said!"





time.sleep(0.5)
x=0
print("start..")
speak("Hi! Anushree,what can I do for you?")
data=recordAudio()
jarvis(data)
speak("turning off the program.")
print("run complete")




















