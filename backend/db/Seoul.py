#-*- coding:utf-8 -*-
# 2019.08.18 import 경로 설정을 단순하게 변경
# import sys
# import os
# dirname = os.path.dirname(__file__)
# sys.path.append(os.path.join(dirname,'../db'))
from sqlalchemy import Column, Integer, String
from .base import Base


class Seoul(Base):
    __tablename__ = 'Seoul'

    id = Column(Integer, primary_key=True)
    location = Column(String)

    def __init__(self, location):
        self.location = location

    def __repr__(self):
        return '<Seoul id=%s location=%s>' % (self.id, self.location)

    # jsonify로 리턴해주기위해 db 클래스 data를 serialize 해주는 메서드 추가
    @property
    def serialize(self):
       return {
           'id': self.id,
           'location': self.location
       }