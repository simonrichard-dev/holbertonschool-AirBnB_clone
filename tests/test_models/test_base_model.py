#!/usr/bin/python3
""" test base """
import unittest
from models.base_model import BaseModel
from io import StringIO


class TestBase(unittest.TestCase):
    """ unittest """

    def test_init(self):
        basemodel = BaseModel()
        basemodel.id = "3th4N - 5im0n"
        self.assertEqual(basemodel.id, "3th4N - 5im0n")
