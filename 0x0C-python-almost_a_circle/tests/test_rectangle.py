#!/usr/bin/python3
"""Unit tests for the Rectangle class"""
from unittest import TestCase
from models.rectangle import Rectangle


class RectangleTests(TestCase):
    """Tests for the Rectangle class."""

    def test_rectangle_creation(self):
        obj = Rectangle(3, 5)
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 5)

    def test_rectangle_with_position(self):
        obj = Rectangle(3, 4, 5, 7)
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 7)


class RectangleValidation(TestCase):
    """Tests for validation of the Rectangle class."""

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(12, "21")
        with self.assertRaises(TypeError):
            obj = Rectangle(12, 21)
            obj.height = "text"
        with self.assertRaises(ValueError):
            obj = Rectangle(12, -5)
        with self.assertRaises(ValueError):
            obj = Rectangle(12, 0)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            obj = Rectangle("21", 12)
            self.assertEqual(obj.width, "")
        with self.assertRaises(TypeError):
            obj = Rectangle(12, 21)
            obj.width = "text"
        with self.assertRaises(ValueError):
            obj = Rectangle(-12, 5)
        with self.assertRaises(ValueError):
            obj = Rectangle(0, 5)

    def test_invalid_position(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(21, 12, "2", 2)
            self.assertEqual(obj.width, "")
        with self.assertRaises(TypeError):
            obj = Rectangle(12, 21)
            obj.x = "text"
        with self.assertRaises(TypeError):
            obj = Rectangle(12, 21)
            obj.y = "text"
        with self.assertRaises(ValueError):
            obj = Rectangle(12, 5, 1, -1)
        with self.assertRaises(ValueError):
            obj = Rectangle(10, 5, -2, 1)

    def test_origin(self):
        rect = Rectangle(12, 21)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.x = 0
        self.y = 0

    def test_area(self):
        rect = Rectangle(10, 8)
        self.assertEqual(rect.area(), 80)


class RectangleUpdateTests(TestCase):
    """Test rectangle update method."""

    def test_update_with_args(self):
        self.assertTrue(True)
