#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
<<<<<<< HEAD


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
=======
import os


class test_state(test_basemodel):
    """ states test class"""

    def __init__(self, *args, **kwargs):
        """ state test class init"""
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
<<<<<<< HEAD
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
=======
        """ testing state name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
