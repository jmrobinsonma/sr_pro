from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('note')

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"{self.username} {self.email}"

class UsersSchema(ma.Schema):
	class Meta:
		fields = ("id", "username", "email", "password")


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

class UsersResource(Resource):
	def get(self):
		users = User.query.all()
		return users_schema.dump(users)

	def post(self):
		args = parser.parse_args()
		new_user = User(username=args['username'], email=args['email'], password=args['password'])
		db.session.add(new_user)
		db.session.commit()
		return user_schema.dump(new_user)

class UserResource(Resource):
	def get(self, post_id):
		user = User.query.get_or_404(post_id)
		return user_schema.dump(user)

	def delete(self, post_id):
		user = User.query.get_or_404(post_id)
		db.session.delete(user)
		db.session.commit()
		return '', 204

#	def put(self, post_id):
#		args = parser.parse_args()
#		note = Notes.query.get_or_404(post_id)
#		note.note = args['note']
#		db.session.commit()
#		return note_schema.dump(note)

api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<int:post_id>')



class Notes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	note = db.Column(db.String())

	def __repr__(self):
		return f"{self.id} {self.note}"


class NotesSchema(ma.Schema):
	class Meta:
		fields = ("id", "note")
		


note_schema = NotesSchema()
notes_schema = NotesSchema(many=True)


class NotesResource(Resource):
	def get(self):
		notes = Notes.query.all()
		return notes_schema.dump(notes)

	def post(self):
		args = parser.parse_args()
		new_note = Notes(note=args['note'])
		db.session.add(new_note)
		db.session.commit()
		return note_schema.dump(new_note)


class NoteResource(Resource):
	def get(self, post_id):
		note = Notes.query.get_or_404(post_id)
		return note_schema.dump(note)

	
	def put(self, post_id):
		args = parser.parse_args()
		note = Notes.query.get_or_404(post_id)
		note.note = args['note']
		db.session.commit()
		return note_schema.dump(note)

	def delete(self, post_id):
		note = Notes.query.get_or_404(post_id)
		db.session.delete(note)
		db.session.commit()
		return '', 204


api.add_resource(NotesResource, '/notes')
api.add_resource(NoteResource, '/notes/<int:post_id>')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='5001')

