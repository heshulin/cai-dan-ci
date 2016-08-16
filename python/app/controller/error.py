from app.bean.secretkey import Secretkey
from app.db import User,error,word,db
from flask import request
import hashlib

class error_service(object):
    def add_error(self):
        form = request.form
        TrueWord = form.get('TrueWord')
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        print(11111)
        print(TrueWord)
        print(UserPhone)
        print(SecretKey)
        user = User.query.filter_by(UserPhone=UserPhone).first()
        word_info = word.query.filter_by(Word=TrueWord).first()
        add_word = error()
        add_word.ErrorTranslation = word_info.Translation
        add_word.ErrorWord = word_info.Word
        add_word.UserId = user.UserId
        db.session.add(add_word)
        db.session.commit()
        array = {
            'state': 1,
            'msg': "成功",
        }
        return array


    def get_error(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        user = User.query.filter_by(UserPhone=UserPhone).first()
        errorlist = error.query.filter_by(UserId=user.UserId).all()
        num = len(errorlist)
        list = []
        for i in range(0,num-1):
            array = {
                'TrueWord':errorlist[i].ErrorWord,
                'Translation':errorlist[i].ErrorTranslasion
            }
            list.append(array)
        array = {
            'state':1,
            'msg':"成功",
            'data':list
        }
        return array