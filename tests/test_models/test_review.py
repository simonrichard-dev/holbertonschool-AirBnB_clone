#!/usr/bin/python3
""" test review """
import unittest
from models.base_model import BaseModel
from models.review import Review

from io import StringIO


class TestReview(unittest.TestCase):
    """ unittest for place file """

    def test_place_id(self):
        review = Review()
        review.place_id = "94102"
        self.assertEqual(review.place_id, "94102")

    def test_user_id(self):
        review = Review()
        review.user_id = "0626839210"
        self.assertEqual(review.user_id, "0626839210")

    def test_text(self):
        review = Review()
        review.text = "Cute place to discover SF near Holberton School"
        self.assertEqual(review.text, "Cute place to discover SF near Holberton School")
