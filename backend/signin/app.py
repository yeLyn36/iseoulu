# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, redirect, escape, session
from service import sign_in


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/createMember', methods=['GET', 'POST'])  # db 넣고 없어질 메소드
def createMember():
    if request.method == 'POST':
        content = request.json
        id = '%s' % escape(session['id'])
        pwd = content['pwd']
        name = content['name']
        email = content['email']
        age = content['age']
        gender = content["gender"]
        data = sign_in.create_member(id, pwd, name, email, age, gender)
        return jsonify(data)
    else:
        return jsonify({"ok": False})

@app.route('/modifyPwd', methods=['GET', 'POST'])  # db 넣고 없어질 메소드
def modifyPwd():
    if request.method == 'POST':
        content = request.json
        id = '%s' % escape(session['id'])
        pwd = '%s' % content['pwd']
        data = sign_in.modify_password(pwd, id)
        return jsonify(data)
    else:
        return jsonify({"ok": False})


@app.route('/modifyAge', methods=['GET', 'POST'])  # db 넣고 없어질 메소드
def modifyAge():
    if request.method == 'POST':
        content = request.json
        id = '%s' % escape(session['id'])
        age = '%s' % content['age']
        data = sign_in.modify_age(age, id)
        return jsonify(data)
    else:
        return jsonify({"ok": False})



@app.route('/deleteMember', methods=['POST', 'GET'])
def review_delete():
    if request.method == 'POST':
        id = '%s' % escape(session['id'])
        pwd = '%s' % escape(session['pwd'])
        result = sign_in.delete(id, pwd)
        print(result)
        return jsonify({"ok": False})
    else:
        return False


if __name__ == "__main__":
    app.run(port=5002, debug=True)
