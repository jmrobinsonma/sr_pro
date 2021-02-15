import os
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
		speak("Good Morning!")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Ambassador !") 

	else:
		speak("Good Evening Ambassador !") 

	assname =("Bee Sixty-nine Four-twenty")


def flask_local(query: str):
	
	url = "127.0.0.1:5000"

	if len(query) == 5:
	 	webbrowser.open(url)
	else:
		print(len(query))
		query.replace("slash", "/")
		query_split = query.split(" ")[1::]
		extension = "".join(query_split)
		webbrowser.open(f"{url}{extension}")



if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()

#	wish_me()
	while True:
		url = "http://127.0.0.1:5001/notes"
		query = take_command().lower()

		if "what's your name" in query or "what is your name" in query:
			speak("My friends call me")
			speak("Bee Sixty-nine Four-twenty")
			print("My friends call me B69420")

		elif 'flask' in query:
			flask_local(query)

		elif 'search' in query or 'play' in query:
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 
		
		elif 'weather' in query:
			webbrowser.open("https://www.accuweather.com/en/us/granby/01033/weather-forecast/2250736")

		elif 'my github' in query:
			webbrowser.open("https://github.com/jmrobinsonma")

		elif 'my website' in query:
			webbrowser.open("www.jmrobinson.online")

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
