#!/usr/bin/python3
""" test amenity """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

from io import StringIO


class TestAmenity(unittest.TestCase):
    """ unittest for amenity file """

    def test_name(self):
        amenity = Amenity()
        amenity.name = ""
        self.assertEqual(amenity.name, "")

    def test_class(self):
        testamenity = Amenity()
        self.assertEqual(testamenity.__class__.__name__, "Amenity")

    def test_subclass(self):
        testamenity = Amenity()
        self.assertTrue(issubclass(testamenity.__class__, BaseModel))

    def test_attributes_Class(self):
        """Test attributes Class """
        my_amenity = Amenity()
        my_amenity.name = "Hello-Holberton"
        self.assertEqual(my_amenity.name, 'Hello-Holberton')
