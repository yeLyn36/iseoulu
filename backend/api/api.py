import json
from urllib import request as ul

concert = []
classic = []
theater = []
musical = []
with open('nogada.json') as json_file:
    json_data = json.load(json_file)
    for i in range(0,314):
        theme = json_data["DATA"][i]["theme"]
        title = json_data["DATA"][i]['title']
        if theme == "콘서트":
            concert.append(title)
        elif theme == "클래식":
            classic.append(title)
        elif theme == "연극":
            theater.append(title)
        elif theme == "뮤지컬/오페라":
            musical.append(title)