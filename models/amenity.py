#!/usr/bin/python3
""" State Module for HBNB project """

"""
Class defines Amenities that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines amenities that user can choose from to offer at its place"""
    name = ""
