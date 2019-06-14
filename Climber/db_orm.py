from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
import datetime
import unittest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///test4.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

""" 
route_sets
- set_id
- date_up
- date_down, nullable=True


routes
- id
- set_id
- grade e.g. green
- sub_grade e.g. up or down

route_meta
- TBD

route_user_data
- id
- route_id
- user_id
- grade_user
- status e.g. done, todo, attempted
- status_special e.g. Target

users
- user_id
- email
etc 

"""


# The two tables of route_set and route have a one to many relationship

class RouteSet(Base):
    __tablename__ = 'route_set'
    id = Column(Integer, primary_key=True)
    up_date = Column(Integer)
    down_date = Column(Integer)
    active = Column(Integer)

    routes = relationship('Route', back_populates='route_set', cascade="all, delete, delete-orphan")


class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    grade_sub = Column(Integer)
    route_set_id = Column(Integer, ForeignKey('route_set.id'))

    # Craete many to one releationship - many routes to a set
    route_set = relationship('RouteSet', back_populates='routes')


class RouteRecord(Base):
    __tablename__ = 'route_records'
    id = Column(Integer, primary_key=True)
    route_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    status = Column(Integer, default=ClimbStatus.get_default())
    count = Column(Integer)
    users = relationship('User', back_populates='route_records')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    route_records = relationship('RouteRecord', back_populates='users', cascade="all, delete, delete-orphan")





rs = RouteSet(up_date=1, down_date=2, active=1)

rs.routes = [Route(grade=Grade.black, grade_sub=GradeSub.low),
             Route(grade=Grade.blue, grade_sub=GradeSub.high)]
# rr = RouteRecord()
Base.metadata.create_all(engine)

session.add(rs)
# session.add(rr)
session.commit()

user_a = User(email='andrewdcar@gmail.com')
user_b = User(email='whomever@gmail.com')
session.add(user_a)
session.add(user_b)
session.commit()
route_rec = RouteRecord(route_id=123, status=1, count=1000)
session.add(route_rec)
session.commit()

