#!/usr/bin/python3

""" Review module for the HBNB project """

"""
Class for user's review that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    """Reviews made by users about a place"""
    place_id = ""
    user_id = ""
    text = ""
