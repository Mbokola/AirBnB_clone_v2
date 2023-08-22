#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """
        getter attribute cities that returns the list of City instances with
        state_id equals to the current State.id
        """
        from models import storage
        instances = storage.all()

        return [city for city in instances.values()
                if city.state_id == self.id]
