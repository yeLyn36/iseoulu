# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from db.base import Base, Session, engine
from db.member import member
from flask import Flask, request, jsonify
import json
# import sqlite3
import pymysql

# conn = sqlite3.connect("../../test.db")
conn = pymysql.connect(
  host = "localhost",
  user = "root",
  password = "mirim2",
  db = "seoulnight",
  charset = "utf8"
)

session = Session()
with open('member.json', mode="r", encoding="utf-8") as member_file:
  member_data = json.load(member_file)
# def get_json(member_json):
#  member_data = request.json(member_json)
  id = member_data['id']
  pwd = member_data['pwd']
  name = member_data['name']
  age = int(member_data['age'])
  gender = member_data['gender']
  email = member_data['email']

def init_db():
  Base.metadata.create_all(engine)
  global session
  session = Session()


def check_member(id): # 회원 중복 체크
  try:
    with conn.cursor() as cur:
      sql = "select * from member having id=%s"
      cur.execute(sql, id)
      rows = cur.fetchall()
      for row in rows:
        if row:
          print("중복된 값이 있습니다.")
          return False
      return True
  finally:
    cur.close()


def return_json(id):
  try:
    with conn.cursor() as cur:
      sql = "select * from member having id=%s"
      cur.execute(sql, id)
      rows = cur.fetchall()
      for row in rows:
        if row:
          data = {
                    "id": row[0],
                    "pwd": row[1],
                    "name": row[2],
                    "email": row[3],
                    "age": row[4],
                    "gender": row[5]
                    }
          return data
  finally:
    cur.close()


def create_member(id, pwd, name, email, age, gender): # json 파일을 받아 입력
  if check_member(id):
    try:
      with conn.cursor() as cur:
        sql = "insert into member (id, pwd, name, email, age, gender) values (%s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (id, pwd, name, email, age, gender))
        conn.commit()
        return jsonify(return_json(id))
    finally:
      cur.close()


def modify_password(pwd, member_id): # 비밀번호 변경
  try:
    with conn.cursor() as cur:
      sql = "update member set pwd=%s where id=%s"
      cur.execute(sql, (pwd, member_id))
      conn.commit()
  finally:
    cur.close()
  return jsonify(return_json(member_id))


def modify_age(age, member_id): # 나이 변경
  try:
    with conn.cursor() as cur:
      sql = "update member set age=%s where id=%s"
      cur.execute(sql, (age, member_id))
      conn.commit()
  finally:
    cur.close()
  return jsonify(return_json(member_id))

def delete(member_id, pwd): #회원 탈퇴
  try:
    with conn.cursor() as cur:
      sql = "DELETE FROM member WHERE id=%s and pwd=%s;"
      cur.execute(sql, (member_id, pwd))
      conn.commit()
      print("회원이 탈퇴되었습니다.")
      return {"ok":True}
  finally:
    cur.close()
