import requests
import json
from flask import render_template, url_for, redirect, request, flash
from app import app
from app.forms import NoteForm, RegistrationForm, LoginForm
#from flask_login import login_required

DB_NOTE_URL = "http://localhost:5001/notes"
DB_USER_URL = "http://localhost:5001/users"

def post_entry(url, new_entry):
	return requests.post(url, new_entry)

@app.route("/", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		users = requests.get(DB_USER_URL)
		email=form.email.data
		password=form.password.data
		for user in users.json():
			if email == user['email'] and password == user['password']:
				return redirect(url_for('notes'))
		else:
			flash("Login unsuccessful", "danger")
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	#logout_user()
	return redirect(url_for('login'))

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		#hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		new_user = dict(username=form.username.data, email=form.email.data, password=form.password.data)
		post_entry(DB_USER_URL, new_user)
		flash(f"Registered {form.username.data}", 'success')
		return redirect(url_for('notes'))
	return render_template('register.html', title='Register', form=form)

@app.route('/notes', methods=['GET','POST'])
#@login_required
def notes():
	results = requests.get(DB_NOTE_URL)
	return render_template('notes.html', results=json.loads(results.text), DB_NOTE_URL=DB_NOTE_URL)

@app.route('/input', methods=['GET','POST'])
def input():
	form = NoteForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			new_note = dict(note=form.note.data)
			post_entry(DB_NOTE_URL, new_note)
			return redirect(url_for('notes'))
	return render_template('input.html', legend='New Note',form=form, DB_NOTE_URL=DB_NOTE_URL)

@app.route('/notes/<int:id>', methods=['GET'])
def note(id):
	new_url = f"{DB_NOTE_URL}/{id}"
	result = requests.get(new_url)
	return render_template('note.html', note=request.form.get('note'), result=json.loads(result.text))

@app.route('/notes/<int:id>/delete', methods=['GET','POST'])
def delete_note(id):
	new_url = f"{DB_NOTE_URL}/{id}"
	result = requests.get(new_url)
	remove_note = requests.delete(new_url)
	return render_template('delete.html', result=json.loads(result.text))

@app.route("/notes/<int:id>/edit", methods=['GET', 'POST'])
def edit_note(id):
	new_url = f"{DB_NOTE_URL}/{id}"
	note = requests.get(new_url)
	form = NoteForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			new_content = dict(note=form.note.data)
			update = requests.put(new_url, new_content)
			return redirect(url_for('notes'))
	elif request.method == 'GET':
		form.note.data = json.loads(note.text)['note']
	return render_template('input.html', title='Edit Note',
						   form=form, legend='Edit Note')
