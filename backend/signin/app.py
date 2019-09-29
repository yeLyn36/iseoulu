# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, redirect, escape, session
from service import sign_in
import json
from socket import *

HOST = "127.0.0.1" #local host
PORT = 5002 #open port 7000 for connection
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept() 
print("Connected by: " , addr)
while True:
    data = conn.recv(1024) 
    print("Received: ", repr(data))
    content = request.json
    print(content)
    conn.sendall(content)
conn.close()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create')  # db 넣고 없어질 메소드
def createMember():
    content = request.json
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


@app.route('/modifyPwd', methods=['GET', 'POST'])  # db 넣고 없어질 메소드
def modifyPwd():
    content = request.json
    id = '%s' % escape(content['id'])
    pwd = '%s' % content['pwd']
    data = sign_in.modify_password(pwd, id)
    return jsonify(data)



@app.route('/modifyAge', methods=['GET', 'POST'])  # db 넣고 없어질 메소드
def modifyAge():
    content = request.json
    id = '%s' % escape(content['id'])
    age = '%s' % content['age']
    data = sign_in.modify_age(age, id)
    return jsonify(data)




@app.route('/delete', methods=['POST', 'GET'])
def deleteMember():
    content = request.json
    id = '%s' % escape(content['id'])
    pwd = '%s' % escape(content['pwd'])
    sign_in.delete(id, pwd)
    return jsonify({"ok": False})


if __name__ == "__main__":
    app.run(port=5002, debug=True)
