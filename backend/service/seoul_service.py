# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from db.base import Session, Base, engine
from db.Seoul import Seoul

session = Session()


def init_db():
    Base.metadata.create_all(engine)
    global session
    session = Session()


def create_location(location):
    print(location)
    newLocation = Seoul(location)
    session.add(newLocation)
    session.commit()
    return newLocation

def get_all():
    locationList = session.query(Seoul).all()
    for i in range(len(locationList)):
        locationList[i] = locationList[i].serialize
    return locationList

def get_location(lc_id):
    location = session.query(Seoul).filter_by(id=lc_id).first()
    location = location.serialize
    return location

def delete(lc_id):
    location = session.query(Seoul).filter_by(id=lc_id).first()
    session.delete(location)
    session.commit()
    return {"remove":True}

if __name__ == '__main__':
  create_location("중구 명동 세종대로 110")