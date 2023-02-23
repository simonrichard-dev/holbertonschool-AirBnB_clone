#!/usr/bin/python3
""" test state """
import unittest
from models.base_model import BaseModel
from models.state import State

from io import StringIO


class TestState(unittest.TestCase):
    """ unittest for state file """

    def test_(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")
