#!/usr/bin/python3
""" test place """
import unittest
from models.base_model import BaseModel
from models.place import Place

from io import StringIO


class TestPlace(unittest.TestCase):
    """ unittest for place file """

    def test_city_id(self):
        place = Place()
        place.city_id = "42"
        self.assertEqual(place.city_id, "42")
    
    def test_user_id(self):
        place = Place()
        place.user_id = "0626839210"
        self.assertEqual(place.user_id, "0626839210")

    def test_name(self):
        place = Place()
        place.name = "San Francisco"
        self.assertEqual(place.name, "San Francisco")
 
    def test_description(self):
        place = Place()
        place.description = "La maison de Julien Barbier"
        self.assertEqual(place.description, "La maison de Julien Barbier")

    def test_number_rooms(self):
        place = Place()
        place.number_rooms = 6
        self.assertEqual(place.number_rooms, 6)

    def test_bathrooms(self):
        place = Place()
        place.number_bathrooms = 3
        self.assertEqual(place.number_bathrooms, 3)

    def test_max_guest(self):
        place = Place()
        place.max_guest = 18
        self.assertEqual(place.max_guest, 18)

    def test_price_by_night(self):
        place = Place()
        place.price_by_night = 300
        self.assertEqual(place.price_by_night, 300)

    def test_latitude(self):
        place = Place()
        place.latitude = 37.77750
        self.assertEqual(place.latitude, 37.77750)

    def test_longitude(self):
        place = Place()
        place.longitude = -122.41639
        self.assertEqual(place.longitude, -122.41639)

    def test_amenity_ids(self):
        place = Place()
        place.amenity_ids = ["Computer", "Wifi", "Coffee Machine"]
        self.assertEqual(place.amenity_ids, ["Computer", "Wifi", "Coffee Machine"])
