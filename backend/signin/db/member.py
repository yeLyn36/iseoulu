#-*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .base import Base
from datetime import datetime

class member(Base):
    __tablename__ = 'member'

    id = Column(String(100), primary_key=True)
    pwd = Column(String(100), unique=True)
    email = Column(String(100))
    name = Column(String(100))
    age = Column(Integer)
    gender = Column(String(100))


    def __init__(self, id, pwd, name, email, age, gender):
        self.id = id
        self.pwd = pwd
        self.email = email
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return (self.id + self.pwd + self.name + self.email + self.age, self.gender)

    # jsonify로 리턴해주기위해 db 클래스 data를 serialize 해주는 메서드 추가
    @property
    def serialize(self):
       return {
           "id": self.id,
           "pwd": self.pwd,
           "email": self.email,
           "name": self.name,
           "age": self.age,
           "gender": self.gender
       }
        