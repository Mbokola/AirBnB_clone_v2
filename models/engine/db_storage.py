#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
import datetime
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """
        class for my dbstorage.
    """
    __engine = None
    __session = None

    username = os.getenv('HBNB_MYSQL_USER')
    password = os.getenv('HBNB_MYSQL_PWD')
    host = os.getenv('HBNB_MYSQL_HOST')
    db = os.getenv('HBNB_MYSQL_DB')
    env = os.getenv('HBNB_ENV')

    self.__engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@{host}/{db}',
            pool_pre_ping=True)

    if env == 'test':
        Base.metadata.drop_all(self.__engine)

    def reload(self):
        """
        Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()
