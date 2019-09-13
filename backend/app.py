# -*- coding: utf-8 -*-

from flask import Flask, render_template,request, jsonify, redirect
from api import api
from service import seoul_service

app = Flask(__name__)

location = [{"id":"1", "place":"중구 명동 세종대로 110"},{"id":"2", "place":"기흥구 강남동로 128"}]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create', methods =['GET','POST'])#db 넣고 없어질 메소드
def create():
    if request.method == 'POST':
        content = request.json
        print(content['location'])
        seoul_service.create_location(content['location'])
        return jsonify({"ok":True})
    else:
        return jsonify({"ok":False})

@app.route('/gomap', methods =['GET','POST'])
def get_location():
    if request.method == 'GET':
        id = int(request.args.get('id'))
        result = seoul_service.get_location(id)
        return jsonify({"ok":result})
    else :
        render_template('map.html')


@app.route('/gomap', methods = ['GET'])
def show_gu(place):
    return render_template('map.html',geocode = api.return_gu(place))


@app.route('/get',methods=['GET'])
def get():
    result = seoul_service.get_all()
    return jsonify({"ok":result})

@app.route('/delete', methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        id = request.args.get('id')
        result = seoul_service.delete(id)
        print(result)
        return jsonify(result) 
    else :
        return False

if __name__=="__main__":
    app.run(port=5002,debug=True)