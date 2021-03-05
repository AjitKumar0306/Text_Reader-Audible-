import pyttsx3
file = open("book.txt", "r")
text = file.read()
speaker = pyttsx3.init()
rate = 140
speaker.setProperty('rate', rate)
speaker.say(text)
speaker.runAndWait()
