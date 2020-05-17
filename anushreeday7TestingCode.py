import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
print("say something!")
audio=r.listen(source)
print("heard")


try:
print("Sphinx thinks you sid " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
print("Sphinx could not understand audio")
except sr.RequestError as e:
print("Sphinx error; {0}.format(e))


try:
print("gppgle speech recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError :
print("could not request results from google speech recognition service; {0}.format(e))




WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"

try:
print("Wit.ai thinks you said " + r.recognize(audio, key =WIT_AI_KEY))
except sr.UnknownValueError:
print("Wit.ai could not understand audio")
except sr.RequestError as e:
print("Could not request results from Wit.ai service; {0}.format(e))



























