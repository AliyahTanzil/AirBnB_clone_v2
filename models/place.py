#!/usr/bin/python3
<<<<<<< HEAD
""" Place Module for HBNB project """
=======
"""
Class defines hosting Place that inherits from BaseModel
"""
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """ A place to stay """
=======
    """Defines Place class"""
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
