#!/usr/bin/python3
""" db_storage module """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class db_storage:
    """ The databsaw storage engine """

    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the class """

        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(f"mysql+mysqldb://{user}:\
{pwd}@{host}/{db_name}", pool_pre_ping=True)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries on the current database session all objects depending
        of the class name
        """
        if cls:
            classes = [cls]
        else:
            classes = [State, City]

        objs = {}
        for cls in classes:
            query_obj = self.__session.query(cls).all()
            for obj in query_obj:
                key = f"{cls.__name__}.{obj.id}"
                objs[key] = obj
        return objs

    def new(self, obj):
        """ adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
