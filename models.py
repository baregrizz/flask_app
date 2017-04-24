from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), unique=False)
    nickname = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    age = db.Column(db.Integer, nullable = True)

class Room(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    roomnum = db.Column(db.String(15), unique=True)
    capacity = db.Column(db.Integer, nullable = False)

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fullname = db.Column(db.String(50), unique=False)
#     nickname = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))