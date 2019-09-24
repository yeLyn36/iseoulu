# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, redirect, escape, session
from map.api import api
from map.service import seoul_service


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create', methods=['GET', 'POST'])  # db 넣고 없어질 메소드
def review_create():
    if request.method == 'POST':
        content = request.json
        id = '%s' % escape(session['id'])
        location = content['location']
        article = content['article']
        star_score = content['star_score']
        seoul_service.create_review(id, location, article, star_score)
        return jsonify()
    else:
        return jsonify({"ok": False})


@app.route('/gomap', methods=['GET', 'POST'])
def get_location():
    if request.method == 'GET':
        gu = request.args.get('gu')
        result = api.return_gu(gu)
        render_template('map.html', result=result)


@app.route('/gomap', methods=['GET'])
def show_gu(place):
    return render_template('map.html', geocode=api.return_gu(place))


@app.route('/get', methods=['GET'])
def get():
    result = seoul_service.get_review()
    return jsonify({"ok": result})


@app.route('/delete', methods=['POST', 'GET'])
def review_delete():
    if request.method == 'POST':
        id = '%s' % escape(session['id'])
        pwd = '%s' % escape(session['pwd'])
        result = seoul_service.delete(id,pwd)
        print(result)
        return jsonify(result)
    else:
        return False


if __name__ == "__main__":
    app.run(port=5002, debug=True)
