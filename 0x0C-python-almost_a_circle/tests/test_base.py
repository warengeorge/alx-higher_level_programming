#!/usr/bin/python3
"""Unit tests for base class."""
from unittest import TestCase


class BaseClassTests(TestCase):
    """Tests for the Base class."""

    def setUp(self):
        super().setUp()
        from models.base import Base
        self.Base = Base

    def tearDown(self):
        super().tearDown()
        self.Base = None

    def test_base_class_creation(self):
        obj = self.Base()
        self.assertEqual(obj.id, 1)
        obj = self.Base(42)
        self.assertEqual(obj.id, 42)

    def test_multiple_base_objects(self):
        obj1 = self.Base()
        obj2 = self.Base()
        obj3 = self.Base()
        obj4 = self.Base(10)
        self.assertEqual(obj1.id, 2)
        self.assertEqual(obj2.id, 3)
        self.assertEqual(obj3.id, 4)
        self.assertEqual(obj4.id, 10)
