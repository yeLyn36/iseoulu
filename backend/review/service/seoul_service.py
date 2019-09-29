# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from db.base import Session, Base, engine
from db.review import review
import json

session = Session()
with open('nogada.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

def init_db():
    Base.metadata.create_all(engine)
    global session
    session = Session()

def create_review(id, location, article, star_score):
    newReview = review(id, location, article, star_score)
    session.add(newReview)
    session.commit()
    return newReview

def get_review():
    reviewlist = session.query(review).all()
    for i in range(len(reviewlist)):
        reviewlist[i] = reviewlist[i].serialize
    return reviewlist

def modify_review(member_id, newArticle):
    newArticle = session.query(review).filter_by(id=member_id).first()
    review.article = newArticle
    session.commit()
    return review

def delete_review(member_id, pwd):
    delete_review = session.query(review).filter_by(member_id=member_id).first()
    session.delete(delete_review)
    session.commit()
    return {"ok":True}
# def create_location(location):
#     print(location)
#     newLocation = Seoul(location)
#     session.add(newLocation)
#     session.commit()
#     return newLocation

# def get_all():
#     locationList = session.query(Seoul).all()
#     for i in range(len(locationList)):
#         locationList[i] = locationList[i].serialize
#     return locationList

# def get_location(lc_id):
#     location = session.query(Seoul).filter_by(id=lc_id).first()
#     location = location.serialize
#     return location

# def delete(lc_id):
#     location = session.query(Seoul).filter_by(id=lc_id).first()
#     session.delete(location)
#     session.commit()
#     return {"remove":True}

if __name__ == '__main__':
  pass
  