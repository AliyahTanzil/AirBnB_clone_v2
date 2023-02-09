#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
<<<<<<< HEAD


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
=======
import os


class test_Amenity(test_basemodel):
    """ amenity test class"""

    def __init__(self, *args, **kwargs):
        """inti the test class """
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
<<<<<<< HEAD
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
=======
        """testing name type """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
>>>>>>> ef3c7e2619eccc55ae67e961455ac3f0408bf41d
