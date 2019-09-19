# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from db.base import Base, Session, engine
from db.member import Member
import json

session = Session()
with open('member.json') as member_file:
  member_data = json.load(member_file)
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

def create_member(): # json 파일을 받아 입력
  newMember = Member(id, pwd, email, name, age, gender)
  session.add(newMember)
  session.commit()
  return newMember
  

def modify_password(pwd, member_id): # 비밀번호 변경
  newPassword = session.query(Member).filter_by(id=member_id).first()
  Member.pwd = newPassword
  session.commit()
  return Member

def modify_age(age, member_id): # 나이 변경
  newAge = session.query(Member).filter_by(id=member_id).first()
  Member.age = newAge
  session.commit()
  return Member

def delete(member_id, pwd): #회원 탈퇴
  delete_member = session.query(Member).filter_by(member_id=member_id).first()
  session.delete(delete_member)
  session.commit()
  return {"ok":True}