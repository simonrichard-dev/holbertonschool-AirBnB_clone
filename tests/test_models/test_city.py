#!/usr/bin/python3
""" test city """
import unittest
from models.base_model import BaseModel
from models.city import City

from io import StringIO


class TestCity(unittest.TestCase):
    """ unittest for city file """

    def test_city_id(self):
        city = City()
        city.state_id = ""
        self.assertEqual(city.state_id, "")
    
    def test_city_name(self):
        city = City()
        city.name = ""
        self.assertEqual(city.name, "")

    def test_instance(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_id(self):
        city = City()
        self.asserEqual(str, type(city.id))
