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
서남 = []

구 = []
themeList = []
timeList = []

with open('nogada.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    for i in range(0,len(json_data)):
        data = json_data["DATA"][i]
        place = data["place"][0:2]
        if place == "도봉" or place == "강북" or place == "노원" or place == "성북":
            강북.append(data)
        elif place == "동대" or place == "중랑" or place == "성동" or place == "광진":
            동서울.append(data)
        elif place == "강동" or place == "송파":
            동남.append(data)
        elif place == "서초" or place == "강남":
            강남.append(data)
        elif place == "동작" or place == "관악" or place == "금천":
            남서울.append(data)
        elif place == "강서" or place == "양천" or place == "영등" or place == "구로":
            서남.append(data)
        elif place == "은평" or place == "마포" or place == "서대":
            서서울.append(data)
        elif place == "종로" or place == "중구" or place == "용산":
            도심.append(data)
    gu = [강북, 동서울, 동남, 강남, 남서울, 서남, 서서울, 도심]


def get_list_theme(geted_theme): #테마별 행사 조회
    for j in range(0,len(json_data["DATA"])):
        theme = [1, 2, 3, 4, 5, 6]
        for i in theme:
            if geted_theme == i:
                themeList.append(json_data["DATA"][i])
                return themeList
    return {"ok":False}


def get_list_time(st_time, en_time): # 파라미터 st_time 시작시간, en_time 종료 시간
    now = datetime.now() # 지금의 datetime
    str_time = now.replace(hour = st_time) # 사용자가 원하는 시작 시간
    end_time = now.replace(hour = en_time) # 사용자가 원하는 종료 시간
    for i in range(0,len(json_data["DATA"])):
        try :
            start = json_data["DATA"][i]["start_date"] + " " + json_data["DATA"][i]["started_at"] + ":00.000000" # 데이터의 시작시간 문자열
            end = json_data["DATA"][i]["end_date"] + " " + json_data["DATA"][i]["finished_at"] + ":00.000000" # 데이터의 종료시간 문자열
            str_at = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
            end_at = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
            if (str_time >= str_at) and (end_time <= end_at): # 12, 14 / 14, 23
                timeList.append(json_data["DATA"][i])
                return timeList
            else : return "해당하는 시간대가 없습니다." # 할 말 없어서 그냥 문자열로 넘김
        except ValueError:
            # cycle = json_data["DATA"][i]["start_date"]
            # if cycle[2] == "년":
                
            # elif cycle[2] == "달" or cycle[2] == "월" or cycle[2] == "주":

            # elif cycle == "상시가능":
            pass
        else:
            return "Error"


def return_gu(place):
    for i in range(0,len(json_data["DATA"])):
        if json_data["DATA"][i]["place"][0:2] == place[0:2]:
            구.append(json_data["DATA"][i])
            return 구
    return {"ok":False}



if __name__=='__main__':
    #print(get_list_time(17,21))
    print(return_gu("종로구 서린동 14-1 청계광장"))
    print()
    print(get_list_theme(2))
