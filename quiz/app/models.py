from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Quiz_list(db.model):
    id = db.Column(db.Integer, primary_key=True)
    qName = db.Column(db.String(128), unique=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#might add questions as seperate table
    q1 = db.Column(db.String(128), unique=True)
    q2 = db.Column(db.String(128), unique=True)
    q3 = db.Column(db.String(128), unique=True)
    q4 = db.Column(db.String(128), unique=True)
    q5 = db.Column(db.String(128), unique=True)
    q6 = db.Column(db.String(128), unique=True)
    q7 = db.Column(db.String(128), unique=True)
    q8 = db.Column(db.String(128), unique=True)
    q9 = db.Column(db.String(128), unique=True)
    q10 = db.Column(db.String(128), unique=True)

def __repr__(self):
        return '{}'.format(self.qName)

class Quiz_answers(db.model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(128), db.ForeignKey('quiz_list.qName'))
    u_name = db.Column(db.String(64), db.ForeignKey('user.username'))
    a1 = db.Column(db.Boolean)
    a2 = db.Column(db.Boolean)
    a3 = db.Column(db.Boolean)
    a4 = db.Column(db.Boolean)
    a5 = db.Column(db.Boolean)
    a6 = db.Column(db.Boolean)
    a7 = db.Column(db.Boolean)
    a8 = db.Column(db.Boolean)
    a9 = db.Column(db.Boolean)
    a10 = db.Column(db.Boolean)

    def __repr__(self):
        return '{}'.format(self.quiz_name)

