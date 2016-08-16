#!usr/bin/python
from flask import Flask
from flask import request
from flask import jsonify
from app.controller.login import dologin
from app.controller.translation_word import Translation_word
from app.controller.register1 import Register1
from app.controller.register2 import Register2
from app.controller.register3 import Register3
from app.controller.error import error_service

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def hello_world():
    return jsonify(dologin())


@app.route('/fanyi', methods=['POST','GET'])
def fanyi():
    translation_word = Translation_word()
    return jsonify(translation_word.get_information_random())

@app.route('/caidanci', methods=['POST','GET'])
def caidanci():
    translation_word = Translation_word()
    return jsonify(translation_word.get_information_lack())



@app.route('/adderror', methods=['POST','GET'])
def adderror():
    error_duixiang = error_service()
    return jsonify(error_duixiang.add_error())


@app.route('/geterror', methods=['POST','GET'])
def geterror():
    error_duixiang = error_service()
    return jsonify(error_duixiang.get_error())

#注册模块-----------------------------------------------注册模块
@app.route('/register1', methods=['POST'])
def register1():
    form = request.form
    UserPhone = form.get('UserPhone')
    register1 = Register1()
    return jsonify(register1.register1(UserPhone))


@app.route('/register2', methods=['POST'])
def register2():
    form = request.form
    UserPhone = form.get('UserPhone')
    CheckCode = form.get('CheckCode')
    register2q = Register2()
    return jsonify(register2q.register2(UserPhone, CheckCode))


@app.route('/register3', methods=['POST'])
def register3():
    form = request.form
    UserPhone = form.get('UserPhone')
    PassWord = form.get('PassWord')
    NickName = form.get('NickName')
    CheckCode = form.get('CheckCode')
    register2q = Register2()
    array = register2q.register2(UserPhone, CheckCode)
    q = int(array['state'])
    if q == 1:
        register3 = Register3()
        print(array)
        return jsonify(register3.register3(UserPhone, PassWord, NickName))
    else:
        print(array)
        return jsonify(array)
# 注册模块结束-----------------------------------------------注册模块结束

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True,port=5001)
