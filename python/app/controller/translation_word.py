from app.db import db, word
import random
from flask import request

class Translation_word(object):

    def get_information_random(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        all_word = word.query.all()
        random_len = len(all_word)
        random_num = random.randint(1, random_len)
        this_word = word.query.filter_by(WordId=random_num).first()
        array = {
            'state':1,
            'msg':"成功",
            'TrueWord':this_word.Word,
            'Translation':this_word.Translation
        }
        return array

    def get_information_lack(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        all_word = word.query.all()
        random_len = len(all_word)
        random_num = random.randint(1, random_len)
        this_word = word.query.filter_by(WordId=random_num).first()
        TrueWord = this_word.Word
        ShowWord = TrueWord
        random_len = len(TrueWord)
        random_num = random.randint(0, random_len-1)
        list1 = TrueWord[0:random_num-1]
        list2 = TrueWord[random_num:len(TrueWord)]
        ShowWord = list1 +"*"+list2

        Letter = TrueWord[random_num-1]
        array = {
            'state': 1,
            'msg': "成功",
            'TrueWord': TrueWord,
            'ShowWord': ShowWord,
            'Letter':Letter
        }
        return array

