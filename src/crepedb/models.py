from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    address = Column(String(255))
    tel = Column(String(11))

class Site(Base):
    __tablename__ = 'sites'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    site_url = Column(String(255))

class Page(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    evaluation = Column(Integer)
    url = Column(String(512))
    genre = Column(String(128))
    site = relationship('Site')
    shop = relationship('Shop')

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    reviewer = Column(String(255))
    evaluation = Column(Integer)
    original_id = Column(Integer)
    page = relationship('Page')
