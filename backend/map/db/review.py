#-*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, Boolean ,DateTime
from .base import Base
from datetime import datetime

class review(Base):
    __tablename__ = 'review'

    id = Column(String)
    location = Column(String)
    article = Column(String)
    star_score = int(2)


    def __init__(self, id, location, article, star_score):
        self.id = id
        self.location = location
        self.article = article
        self.star_score = star_score

    def __repr__(self):
        return (self.id + self.location+self.article+self.star_score)

    @property
    def serialize(self):
       return {
           'id': self.id,
           'location': self.location,
           'article': self.article,
           'star_score': self.star_score
       }