# -*- coding:utf-8 -*-

import json
from datetime import datetime

gangbuk = []
dongseoul = []
dongnam = []
gangnam = []
dosim = []
namseoul = []
seoseoul = []
seonam = []
gu1 = []
themeList = []
timeList = []


with open('nogada.json', encoding="utf-8") as json_file:
    json_data = json.load(json_file)
    for i in range(0, len(json_data['DATA'])):
        data = json_data["DATA"][i]
        place = data["place"][0:2]
        if place == "도봉" or place == "강북" or place == "노원" or place == "성북":
            gangbuk.append(data['place'])
        elif place == "동대" or place == "중랑" or place == "성동" or place == "광진":
            dongseoul.append(data['place'])
        elif place == "강동" or place == "송파":
            dongnam.append(data['place'])
        elif place == "서초" or place == "":
            gangnam.append(data['place'])
        elif place == "동작" or place == "관악" or place == "금천":
            namseoul.append(data['place'])
        elif place == "강서" or place == "양천" or place == "영등" or place == "구로":
            seonam.append(data['place'])
        elif place == "은평" or place == "마포" or place == "서대":
            seoseoul.append(data['place'])
        elif place == "종로" or place == "중구" or place == "용산":
            dosim.append(data['place'])
    seoul = {'강북':gangbuk,'동서울':dongseoul,'동남':dongnam, '강남':gangnam,'남서울':namseoul,'서남':seonam,'서서울':seoseoul,'도심':dosim}


def get_list_theme(geted_theme): #테마별 행사 조회
    for i in range(0,len(json_data["DATA"])):
        for j in range(len(json_data["DATA"][i]["theme"])):
            if geted_theme == json_data["DATA"][i]["theme"][j]:
                themeList.append(json_data["DATA"][i])
    return themeList


def get_list_time(st_time, en_time):  # 파라미터 st_time 시작시간, en_time 종료 시간
    now = datetime.now()  # 지금의 datetime
    str_time = now.replace(hour=st_time)  # 사용자가 원하는 시작 시간
    end_time = now.replace(hour=en_time)  # 사용자가 원하는 종료 시간
    for i in range(0, len(json_data["DATA"])):
        try:
            start = json_data["DATA"][i]["start_date"] + " " + \
                json_data["DATA"][i]["started_at"] + \
                ":00.000000"  # 데이터의 시작시간 문자열
            end = json_data["DATA"][i]["end_date"] + " " + \
                json_data["DATA"][i]["finished_at"] + \
                ":00.000000"  # 데이터의 종료시간 문자열
            str_at = datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
            end_at = datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
            if (str_time >= str_at) and (end_time <= end_at):  # 12, 14 / 14, 23
                timeList.append(json_data["DATA"][i])
                return timeList
            else:
                return "해당하는 시간대가 없습니다."  # 할 말 없어서 그냥 문자열로 넘김
        except ValueError:
            # cycle = json_data["DATA"][i]["start_date"]
            # if cycle[2] == "년":

            # elif cycle[2] == "달" or cycle[2] == "월" or cycle[2] == "주":

            # elif cycle == "상시가능":
            pass
        else:
            return "Error"


def return_gu(gu):
    for j in seoul.keys():  # seoul은 gangbuk, dongseoul 그딴 거 묶어놓은 리스트
        print(gu)
        if gu == str(j):
            return seoul[j]
    return gu1


if __name__ == '__main__':
    # print(get_list_time(17,21))
    print(return_gu("도심"))
    print()
   # print(get_list_theme(2))
