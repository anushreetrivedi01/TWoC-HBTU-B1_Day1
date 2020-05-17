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
while

























































