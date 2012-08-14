#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

Base = declarative_base()

class Livre(Base):
    __tablename__ = 'livres'
    id = Column(Integer, primary_key = True)
    auteur = Column(String)
    titre = Column(String)
    genre = Column(String)

    def __init__(self, auteur, titre, genre):
        self.auteur = auteur
        self.titre = titre
        self.genre = genre

