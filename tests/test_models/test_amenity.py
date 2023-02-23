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
        amenity.name = "Computer"
        self.assertEqual(amenity.name, "Computer")
