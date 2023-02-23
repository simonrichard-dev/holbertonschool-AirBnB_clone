#!/usr/bin/python3
""" test user """
import unittest
from models.base_model import BaseModel
from models.user import User

from io import StringIO


class TestUser(unittest.TestCase):
    """ unittest for user file """

    def test_email(self):
        user = User()
        user.email = "julien.barbier@holbertonschool.com"
        self.assertEqual(user.email, "julien.barbier@holbertonschool.com")

    def test_password(self):
        user = User()
        user.password = "Ethan1709"
        self.assertEqual(user.password, "Ethan1709")

    def test_first_name(self):
        user = User()
        user.first_name = "Julien"
        self.assertEqual(user.first_name, "Julien")

    def test_last_name(self):
        user = User()
        user.last_name = "Barbier"
        self.assertEqual(user.last_name, "Barbier")
