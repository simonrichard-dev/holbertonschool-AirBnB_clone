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
        self.assertEqual("", review.place_id)

    def test_user_id(self):
        review = Review()
        self.assertEqual("", review.user_id)

    def test_text(self):
        review = Review()
        review.text = ""
        self.assertEqual(review.text, "")

    def test_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)
