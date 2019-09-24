# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from db.base import Base, Session, engine
from db.member import member
from flask import request, jsonify, current_app
import json
import sqlite3

conn = sqlite3.connect("../../test.db")

session = Session()
with open('member.json', mode="r", encoding="utf-8") as member_file:
  member_data = json.load(member_file)
#def get_json(member_json):
#  member_data = request.json(member_json)
  id = member_data['id']
  pwd = member_data['pwd']
  name = member_data['name']
  age = member_data['age']
  gender = member_data['gender']
  email = member_data['email']

def init_db():
  Base.metadata.create_all(engine)
  global session
  session = Session()


def check_member(id):
  try:
    cur = conn.cursor()
    cur.execute("select * from member where id=?", (id, ))
    rows = cur.fetchall()
    for row in rows:
      if row:
        print("중복된 값이 있습니다.")
        return False
    return True
  finally:
    cur.close()


def create_member(id, pwd, name, email, age, gender): # json 파일을 받아 입력
  if check_member(id) :
    newMember = member(id, pwd, name, email, age, gender)
    session.add(newMember)
    session.commit()
    return jsonify(newMember)


def modify_password(pwd, member_id): # 비밀번호 변경
  cur = conn.cursor()
  cur.execute("update member set pwd=? where id=?", (pwd, member_id, ))
  session.commit() 
  cur.close()
  return jsonify(member)

def modify_age(age, member_id): # 나이 변경
  newAge = session.query(member).filter_by(id=member_id).first()
  member.age = newAge
  session.commit()
  return jsonify(member)

def delete(member_id, pwd): #회원 탈퇴
  delete_member = session.query(member).filter_by(id=member_id).first()
  session.delete(delete_member)
  session.commit()
  return {"ok":True}

if __name__ == '__main__':
  print(id)
  print(pwd)
  print(name)
  print(age)
  print(email)
  print(gender)
  create_member(id, pwd, name, email, age, gender)
  # modify_password("perse", id)
  # modify_age(20, id)
  # delete(id, pwd)