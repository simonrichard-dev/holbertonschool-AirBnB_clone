#!/usr/bin/python3
""" test state """
import unittest
from models.base_model import BaseModel
from models.state import State

from io import StringIO


class TestState(unittest.TestCase):
    """ unittest for state file """

    def test_name(self):
        state = State()
        self.assertEqual("", state.name)

    def test_instance(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_id(self):
        state = State()
        self.assertEqual(str, type(state.id))
