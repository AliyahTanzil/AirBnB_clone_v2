#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
<<<<<<< HEAD


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
=======
import os


class test_City(test_basemodel):
    """ tests for city """

    def __init__(self, *args, **kwargs):
        """ init the test class"""
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
<<<<<<< HEAD
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
=======
        """ testing state_id type """
        new = self.value()
        self.assertEqual(type(new.state_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """ testing name type"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
