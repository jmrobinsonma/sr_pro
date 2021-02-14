import datetime
import pyttsx3
import pyjokes
import requests
import webbrowser
import wikipedia
import speech_recognition as sr  


engine = pyttsx3.init("espeak")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
speed = engine.getProperty('rate')
engine.setProperty('rate', 145)

def take_command():
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio)
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	return query

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wish_me():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Ambassador !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Ambassador !") 

	else:
		speak("Good Evening Ambassador !") 

	assname =("Bee Sixty-nine Four-twenty")


if __name__ == '__main__':
	
#	wish_me()
	while True:
		url = "http://127.0.0.1:5001/notes"
		query = take_command().lower()

		if "what's your name" in query or "what is your name" in query:
			speak("My friends call me")
			speak("Bee Sixty-nine Four-twenty")
			print("My friends call me B69420")

		elif 'search' in query or 'play' in query:
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 
		
		elif 'weather' in query:
			speak("Opening accuweather")
			webbrowser.open("accuweather.com")

		elif 'joke' in query:
			joke = pyjokes.get_joke()
			print(joke)
			speak(joke)

		elif "take note" in query:
			speak("What should i write")
			note = take_command()
			data = {"note": note}
			send_note = requests.post(url, data)
			speak("Note saved")

		elif "show notes" in query:
			speak("Showing Notes")
			response = requests.get(url)
			for item in response.json():
				print(f"\n{item['id']}: {item['note']}")
				speak(item['id'])
				speak(item['note'])	
		
		elif "delete note" in query:
			try:
				speak("Which note?")
				note_id = take_command()
				delete_url = f"{url}/{int(note_id)}"
				response = requests.delete(delete_url)
				print(response.status_code)
				if response.status_code == 204:
					speak(f"Note {note_id} deleted")
				else:
					speak(f"{note_id} appears to be an invalid index. Please try again")
			except Exception:
				speak("There was an error, please try again")

		elif 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'exit' in query:
			speak("Exiting now")
			exit()				

"""

import subprocess
#import wolframalpha
#import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
#import winshell
import pyjokes
#import feedparser
import smtplib
#import ctypes
import time
import requests
import shutil
#from twilio.rest import Client
#from clint.textui import progress
#from ecapture import ecapture as ec
from bs4 import BeautifulSoup
#import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Ambassador !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Ambassador !") 

	else:
		speak("Good Evening Ambassador !") 

	assname =("Bee Sixty-nine Four-twenty")
	speak("I am your Assistant")
	speak(assname)
	

def usrname():
	speak("What should i call you Ambassador")
	uname = takeCommand()
	speak("Welcome Ambassador")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Ambassador", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Ambassador")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query



if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	usrname()
	
	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be 
		# stored here in 'query' and will be
		# converted to lower case for easily 
		# recognition of command
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com") 

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("% H:% M:% S") 
			speak(f"Sir, the time is {strTime}")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query: 
			speak("I have been created by Gaurav.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			
#		elif "calculate" in query: 
#			
#			app_id = "Wolframalpha api id"
#			client = wolframalpha.Client(app_id)
#			indx = query.lower().split().index('calculate') 
#			query = query.split()[indx + 1:] 
#			res = client.query(' '.join(query)) 
#			answer = next(res.results).text
#			print("The answer is " + answer) 
#			speak("The answer is " + answer) #

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 

		elif "who i am" in query:
			speak("If you talk then definately your human.")

		elif "why you came to world" in query:
			speak("Thanks to Gaurav. further It's a secret")

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by Gaurav")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Mister Gaurav ")


		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")


		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r") 
			print(file.read())
			speak(file.read(6))

				
		# NPPR9-FWDCX-D2C8J-H872K-2YT43
		elif "jarvis" in query:
			
			wishMe()
			speak("Jarvis 1 point o in your service Mister")
			speak(assname)

		elif "weather" in query:
			webbrowser.open("accuweather.com")
#			
#			# Google Open weather website
#			# to get API of Open weather 
#			api_key = "Api key"
#			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
#			speak(" City name ")
#			print("City name : ")
#			city_name = takeCommand()
#			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
#			response = requests.get(complete_url) 
#			x = response.json() 
#			
#			if x["cod"] != "404": 
#				y = x["main"] 
#				current_temperature = y["temp"] 
#				current_pressure = y["pressure"] 
#				current_humidiy = y["humidity"] 
#				z = x["weather"] 
#				weather_description = z[0]["description"] 
#				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
#			
#			else: 
#				speak(" City Not Found ")
			
		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query: 
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("It's hard to understand")

#		elif "what is" in query or "who is" in query:
			
			# Use the same API key 
			# that we have generated earlier
#			client = wolframalpha.Client("API_ID")
#			res = client.query(query)
#			
#			try:
#				print (next(res.results).text)
#				speak (next(res.results).text)
#			except StopIteration:
#				print ("No results")

		# elif "" in query:
			# Command go here
			# For adding more commands

"""