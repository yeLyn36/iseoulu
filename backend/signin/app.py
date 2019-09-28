# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, redirect, escape, session
from service import sign_in
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create', methods=['GET', 'POST'])  # db 넣고 없어질 메소드
def createMember():
    if request.method == 'POST':
        # content = request.json
        with open('member.json', encoding="utf-8") as member:
            content = json.load(member)
            id = '%s' % escape(content['id'])
            pwd = content['pwd']
            name = content['name']
            email = content['email']
            age = content['age']
            gender = content["gender"]
            data = sign_in.create_member(id, pwd, name, email, age, gender)
            if data is None:
                return "중복되었습니다."
            return jsonify(data)
    else:
        return "hi"
        #jsonify({"ok": False})

@app.route('/modifyPwd', methods=['GET', 'POST'])  # db 넣고 없어질 메소드
def modifyPwd():
    if request.method == 'POST':
        with open('member.json', encoding="utf-8") as member:
            content = json.load(member)
        # content = request.json
            id = '%s' % escape(content['id'])
            pwd = '%s' % content['pwd']
            data = sign_in.modify_password(pwd, id)
            return jsonify(data)
    else:
        return jsonify({"ok": False})


@app.route('/modifyAge', methods=['GET', 'POST'])  # db 넣고 없어질 메소드
def modifyAge():
    if request.method == 'POST':
        # content = request.json
        with open('member.json', encoding="utf-8") as member:
            content = json.load(member)
            id = '%s' % escape(content['id'])
            age = '%s' % content['age']
            data = sign_in.modify_age(age, id)
            return jsonify(data)
    else:
        return jsonify({"ok": False})



@app.route('/delete', methods=['POST', 'GET'])
def deleteMember():
    if request.method == 'POST':
        with open('member.json', encoding="utf-8") as member:
            content = json.load(member)
            id = '%s' % escape(content['id'])
            pwd = '%s' % escape(content['pwd'])
            sign_in.delete(id, pwd)
            return jsonify({"ok": False})
    else:
        return False


if __name__ == "__main__":
    app.run(port=5002, debug=True)
