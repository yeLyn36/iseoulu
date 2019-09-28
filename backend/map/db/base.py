#-*- coding:utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# 2019.08.18 sqlite db를 in memory에서 file로 변경 (절대경로 사용)
# db_host = os.environ.get('DB_HOST', 'sqlite:///:memory:')
db_path = os.path.join(os.path.abspath('../../test.db'))
db_host = os.environ.get('DB_HOST', 'sqlite:///' + db_path)

engine = create_engine(db_host)
# 2019.08.18 세션 유지를 위해 scoped_session을 추가
Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()