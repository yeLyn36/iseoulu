# -*- coding: utf-8 -*-

from db.base import Base, Session, engine
from db.member import Member
import json

with open('member.json') as member_file:
    member_data = json.load(member_file)
    id = member_data['id']
    pwd = member_data['pwd']
    name = member_data['name']
    age = member_data['age']
    gender = member_data['gender']
    email = member_data['email']

def create_member(): # json 파일을 받아 입력
  pass

def modify(): # 이름, 나이, 성, 비밀번호 변경
  pass

def get() : # 입력한 요소들을 json파일로 보냄
  pass

def delete(): #회원 탈퇴
  pass