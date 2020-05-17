import webbrowser as wb
import speech_recognition as sr
from tkinter import*
from time import ctime
import time
import os
import gtts import gTTs
import pygame
from pygame import mixer


def speak(audioString):
global x
b=audioString
if len(b) == 0
return
tts = gTTs(text=b,lang='en-us')
tts.save("voice%s.mp3"%(x))
pygame.init()
pygame.display.set_mode((2,1))
mixer.music.load("voice%ss.mp3" %(x))
mixer.music.play(0)

x += 1

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
pygame.event.poll()
clock.tick(10)

def recognizeSpeech():
r=sr.Recognizer()
with sr.Microphone() as source:
print("speak...")
audio=r.listen(source)
print("heard...")
data=""


try:
data=r.recognize_google(audio)
priny("you said :" + data)
except sr.UnknownValueError:
print(google speech recognition could not understand audio")
except sr.RequestError as e:
print("could not request results from google search recognition service; {0}".format(e))
return data


def jarvis(data):
speak("i am fine")

elif "what time is it" in data:
speak(time())

elif "where is" in data:
data=data.split(" ")
location= data[2]
speak("hold on anushree,i will show you where" + location + "is.")
wb.open_new_tab("https://www.google.nl/maps/place/" + location + "&amp;")
else:
speak(",,,,,,,i did not get what you said!")


      
      root = Tk()
      
      rootr.title("Assistant")
      root.geometry("400*400")
      x=0
      
      w=Label(root,text = "hi,what can we do for youGHT ?",takefocus = True,font=").pack(side=LEFT)
              
              but2 = Button(text="quit", command=root.quit, activebackground= "white",bg = "red", fg= "white",height=2,width=10).pack(side = RIGHT)
              but1 = Button(text = 'listen','bd=4,command= recordAudio,height=2,width=10,activebackground= "lightreen").pack(side= RIGHT)

      
      
      
      root.mainloop()
      
      
