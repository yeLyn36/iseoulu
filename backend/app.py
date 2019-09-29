from flask import Flask, render_template,request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/gomap')
def map():
    return render_template("map.html")


if __name__=="__main__":
    app.run(port=5002, debug= True)