#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
        TestMaxInteger class
    """

    def test_negative(self):
        """
            Checks if function can give the highest negative
            integer
        """
        self.assertEqual(max_integer([-2, -4, -1, -5]), -1)

    def test_positive(self):
        """
            Checks if function can give the highest positive
            integer
        """
        self.assertEqual(max_integer([2, 4, 1, 5]), 5)

    def test_positive_float(self):
        """
            Checks if function can give the highest positive
            float
        """
        self.assertEqual(max_integer([2.75, 4.25, 1.25, 5.5]), 5.5)

    def test_neg_float(self):
        """
            Checks if function can give the highest negative
            float
        """
        self.assertEqual(max_integer([-2.75, -4.25, -1.25, -5.5]), -1.25)

    def test_char(self):
        """
            Checks if function can give the highest string
        """
        self.assertEqual(max_integer(['a', 'A', 'r', 'R']), 'r')

    def test_strings(self):
        """
            Checks if function can give the highest string
        """
        self.assertEqual(max_integer(['area', 'Aert', 'rain', 'Rad']), 'rain')
        self.assertEqual(max_integer('Zenith'), 't')

    def test_empty_str(self):
        """
            Checks if function can handle empty string
        """
        self.assertEqual(max_integer(""), None)

    def test_max_integer(self):
        """Test for the max_integer in the max_integer module"""

        self.assertEqual(max_integer([1, 4, 5, 3]), 5)
        self.assertEqual(max_integer([1]), 1)

    def test_if_negative_int_in_list(self):
        """Test for the negative interger in list function"""

        self.assertEqual(max_integer([0, -3, -2]), 0)

    def test_if_all_negative_interger(self):
        """Test if all arguments are negative"""

        self.assertEqual(max_integer([-2, -4, -6, -19]), -2)

    def test_if_list_empty(self):
        """Test for if list is empty"""

        self.assertIsNone(max_integer([]))

    def test_if_no_args(self):
        """Test for if no args is provided"""

        self.assertIsNone(max_integer())

    def test_if_none_is_arg(self):
        """Test for if none is provided"""

        self.assertRaises(TypeError, max_integer, None)

    def test_if_a_wrong_type_in_list(self):
        """Test for if a wrong type is provided"""

        self.assertRaises(TypeError, max_integer, [1, 2, "Alx"])

    def test_if_float_is_in_list(self):
        """Test for if float is provided"""

        self.assertEqual(max_integer([-1.4, 3.8, 3.9, 1.5]), 3.9)


if __name__ == "__main__":
    unittest.main()

