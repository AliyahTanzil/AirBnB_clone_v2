#!/usr/bin/python3
<<<<<<< HEAD
""" City Module for HBNB project """
=======

"""
Class defines city that inherits from BaseModel
"""
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
from models.base_model import BaseModel


class City(BaseModel):
<<<<<<< HEAD
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
=======
    """City class inherits from BaseModel
    Attributes:
        state_id (str): Public class attribute for city's state_id
        name (str): Public class attribute for city's name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init method for city class
        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
