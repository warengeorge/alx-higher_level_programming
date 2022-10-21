#!/usr/bin/python3
"""
Function that prints name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints
    My name is <first name> <last name>
    first_name: String
    last_name: String
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
