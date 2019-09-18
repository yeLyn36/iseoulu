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

def review():



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
  