from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader#maybe need this
def load_user(id):
    return User.query.get(int(id))


class Quiz(db.Model):
    quizname = db.Column(db.String(64), primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    q1 = db.Column(db.String(256))
    q2 = db.Column(db.String(256))
    q3 = db.Column(db.String(256))

    
class Qanswers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(64))
    submit_name = db.Column(db.String(64)) #name the non-user chose to submit the questions with (screen name)
    a1 = db.Column(db.String(256))
    a2 = db.Column(db.String(256))
    a3 = db.Column(db.String(256))
    q1copy = db.Column(db.String(256))  #repeated fields for when reviewing results
    q2copy = db.Column(db.String(256))  #this could be done with joins but is simpler this way
    q3copy = db.Column(db.String(256))
    
