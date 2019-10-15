from time import ctime
import time
import os
from gtts import gTTS
global name
import pyttsx3
import speech_recognition as sr
import playsound
import pyautogui
import webbrowser
import psutil
import bs4 as bs
from playsound import playsound

def speak2(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()

def op(data):
	d=data.split(" ")

	ams=""
	for i in range(1,len(d)):
		if d[i]=='dot':
			d[i]='.'
		ams+=d[i]
	print("ams"+ams)	
	pyautogui.typewrite(['winleft'],0.5)
	pyautogui.typewrite(ams)
	pyautogui.typewrite(['enter'])

def q():
    speak2("Anything else? Yes or No")
    d=recordaudio()
    if 'nothing' in d or 'no' in d:
        speak2("okay bye")
        exit()

def type(data):
	speak2("Start typing from current cursor position")
	d=data.split(" ")
	for i in range(1,len(d)):
		pyautogui.typewrite(d[i]+" ")
	speak2("Done Typing")

def webop(data):

	d=data.split(" ")
	ans="www."
	for i in range(2,len(d)):
		ans+=d[i]
	print(ans)
	webbrowser.open(ans)
def readf(data):
	try:
		mf = open(data, "r+")
		d=mf.read()
		speak2("Your file contains")
		speak2(d)
		speak2("Finished")
	except IOError:
		
		speak2("Your file contains")
		speak2(d)
		speak2("Finished")
	except FileNotFoundError:
		speak2("The file was not found! Creating new file")
		nf=open((data+".txt"),'w+')
		speak2("File created!")



def command(data):
	if 'open' in data.lower():
		if 'website' in data.lower():
			webop(data)
			speak2('opened')
			q()
		else:
			op(data)
			speak2('opened')
			q()
	elif 'type' in data.lower() or 'write' in data.lower():
		type(data)
		q()
	elif 'close' in data.lower():
		pyautogui.hotkey('ctrl','w')
		q()
	elif 'search' in data.lower():
		d=data.split(" ")
		webbrowser.open("www.google.com")
		ans=""
		for i in range(1,len(d)):
			ans+=d[i]+" "
		pyautogui.typewrite(ans)
		pyautogui.typewrite(['enter'])
		q()
	elif 'read' in data.lower():
		d=data.split(" ")
		ans=""
		for i in range(1,len(d)):
			if d[i]=='dot':
				d[i]='.'
			ans+=d[i]
		readf(ans)
		q()
	elif 'nothing' in data.lower():
		exit()

def recordaudio():
	
	r=sr.Recognizer()
	with sr.Microphone() as source:
		r.energy_threshold = 50
		r.dynamic_energy_threshold = False
		#r.adjust_for_ambient_noise(source)
		playsound("beep-07.mp3")
		audio=r.listen(source,phrase_time_limit = 8)
		playsound("beep-07.mp3")
	data=" "
	try:
		data=r.recognize_google(audio,language="en")
		print(data)
		
	except sr.UnknownValueError:
		print("Couldn't understand!")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
	return data

speak2("Hi, What is your name? ")
name=recordaudio()
speak2("Welcome"+name)
while(1):
    speak2("What should I do for you?")
    data=recordaudio()
    command(data)

