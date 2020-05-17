import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
print("say something!")
audio=r.listen(source)
try:
print("google speech recognition thinks you said "+r.recognize_google(audio))
except sr.UnknownValueError:
print("google search recognition could not understand audio")
except sr.ReequestError as e:
print("could not request results from google speech recognition service; {0}".format(e))
