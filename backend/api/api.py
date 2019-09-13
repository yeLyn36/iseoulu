#-*- coding:utf-8 -*-

import json
from datetime import datetime

강북 = []
동서울 = []
동남 = []
강남 = []
도심 = []
남서울 = []
서서울 = []
동남 = []
timeList = []

# 저 이제 뭐하죠 어제 또 뭐 필요하다고 했더라
with open('nogada.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    for i in range(0,len(json_data)):
        theme = json_data["DATA"][i]["theme"]
        title = json_data["DATA"][i]['title']
       

def get_list_theme(self, geted_theme): #테마별 행사 조회
    for j in range(0,len(json_data)):
        for i in theme:
            if geted_theme == i:
                return json_data["DATA"][j]
    return {"ok":False}

def get_list_time(st_time, en_time): # 파라미터 st_time 시작시간, en_time 종료 시간
    now = datetime.now() # 지금의 datetime
    str_time = now.replace(hour = st_time) # 사용자가 원하는 시작 시간
    end_time = now.replace(hour = en_time) # 사용자가 원하는 종료 시간
    for i in range(0,len(json_data)):
        start = json_data["DATA"][i]["start_date"] + " " + json_data["DATA"][i]["started_at"] + ":00.000000" # 데이터의 시작시간 문자열
        end = json_data["DATA"][i]["end_date"] + " " + json_data["DATA"][i]["finished_at"] + ":00.000000" # 데이터의 종료시간 문자열
        str_at = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
        end_at = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
        if (str_time >= str_at) and (end_time <= end_at): # 12, 14 / 14, 23
            timeList.append(json_data["DATA"][i])
            return timeList
        else : return "해당하는 시간대가 없습니다." # 할 말 없어서 그냥 문자열로 넘김

def return_gu():
    for i in range(0,len(json_date):
        data = json_data["DATA"][i]
        place = data["place"][0:2]
        if place == "도봉" or place == "강북" or place == "노원" place == "성북":
            강북.append(data)
        elif place = 


if __name__=='__main__':
    print(get_list_time(17,21))

    
    