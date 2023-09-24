from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from os import getenv
import models

place_amenity_association = Table('place_amenity', Base.metadata,
                                  Column('place_id', String(60),
                                         ForeignKey('places.id'),
                                         primary_key=True,
                                         nullable=False),
                                  Column("amenity_id", String(60),
                                         ForeignKey("amenities.id"),
                                         primary_key=True,
                                         nullable=False))


class Place(BaseModel, Base):
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship("Amenity", secondary=place_amenity_association,
                                 back_populates="place_amenities")

    else:
        @property
        def reviews(self):
            """Getter attribute for file storage"""
            return [review for review in models.storage.all(Review)
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Amenity getter from file storage"""
            return [amenity for amenity in models.storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
