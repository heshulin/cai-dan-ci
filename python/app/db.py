from app import app
from flask import Flask
from flask_script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
import pymysql

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@183.175.14.250:3306/loveu'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)

class error(db.Model):
    ErrorId = db.Column(db.Integer, primary_key=True)
    ErrorWord = db.Column(db.String)
    ErrorTranslation = db.Column(db.String)
    UserId = db.Column(db.Integer)
    def __repr__(self):
        return '<User %r>' % self.UserId

class word(db.Model):
    WordId = db.Column(db.Integer,primary_key=True)
    Word  = db.Column(db.String)
    Translation = db.Column(db.String)
    def __repr__(self):
        return '<User %r>' % self.Word

class User(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    UserPhone = db.Column(db.String)
    PassWord = db.Column(db.String)
    NickName = db.Column(db.String)
    TrueName = db.Column(db.String)
    UserSex = db.Column(db.Integer)
    UserGrade = db.Column(db.String)
    UserPhoto = db.Column(db.String)
    SecretKey = db.Column(db.String)
    UserMajor = db.Column(db.String)
    Experience = db.Column(db.Integer)
    Token = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.UserPhone


class Checkcode(db.Model):
    CheckId = db.Column(db.Integer, primary_key=True)
    UserPhone = db.Column(db.String)
    CheckCode = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.UserPhone + "&" + str(self.CheckCode)