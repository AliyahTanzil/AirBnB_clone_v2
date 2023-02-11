#!/usr/bin/python3

"""This module defines a class User"""

"""
User class creation that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):

    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    """Defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
