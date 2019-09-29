#-*- coding:utf-8 -*-

import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mirim2', db='seoulnight', charset='utf8')
cursor = db.cursor()


def review(id, location, article, star_score):
    cursor = db.cursor()
    sql = "INSERT INTO review (id, location, article, star_score) VALUES ('"+id+"','"+location+"','"+article+"',"+str(star_score)+");"
    cursor.execute(sql)
    db.commit()
    db.close()

def get_review(location):
    sql = "select * from review where location = " + location
    cursor.execute(sql)
    db.commit()
    db.close()

if __name__ == '__main__':
    review("nam","seoul","안뇽",5)


