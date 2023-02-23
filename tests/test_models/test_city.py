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
        city.state_id = "42"
        self.assertEqual(city.state_id, "42")
    
    def test_city_name(self):
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")   
