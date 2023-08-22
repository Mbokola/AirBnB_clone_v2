#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    env = os.getenv('HBNB_ENV')
