#!/usr/bin/python3
""" test amenity """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

from io import StringIO


class TestAmenity(unittest.TestCase):
    """ unittest for amenity file """

    def test_(self):
        amenity = Amenity()
        amenity.name = ""
        self.assertEqual(amenity.name, "")

    def test_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_id(self):
        amenity = Amenity()
        self.assertEqual(str, type(amenity.id))
