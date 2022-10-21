==========================================
Tests for the 0-add_integer module
==========================================

This module has only one function which is the ``add_integer()``
function which accepts an integer or float and return the sum in integer.
Raise an ``exception`` if the argument is not an int or float.

Importing the ``add_integer()`` function
=========================================
        >>> add_integer = __import__("0-add_integer").add_integer

checking for module docstring
::
        >>> mod_string = __import__("0-add_integer").__doc__
        >>> len(mod_string) > 5
        True

checking for function docstring
::
        >>> fun_docs = add_integer.__doc__
        >>> len(fun_docs) > 5
        True

checking addition of positive integer
::
        >>> add_integer(3, 2)
        5
        >>> add_integer(20000, 40000)
        60000

checking addition of negative integers
::
        >>> add_integer(-4, -2)
        -6

checking addition of both positive and negative integers
::
        >>> add_integer(1, -3)
        -2

checking addition of floats
::
        >>> add_integer(2.43, 0.32)
        2
        >>> add_integer(4.0/2.0, 5)
        7
        >>> add_integer(5.0, float("nan"))
        Traceback (most recent call last):
        ValueError: cannot convert float NaN to integer
        >>> add_integer(float("inf"), 3)
        Traceback (most recent call last):
        OverflowError: cannot convert float infinity to integer

checking addition of strings
::
        >>> add_integer(" ", 5)
        Traceback (most recent call last):
        TypeError: a must be an integer
        >>> add_integer("cup")
        Traceback (most recent call last):
        TypeError: a must be an integer
        >>> add_integer(20, "ten")
        Traceback (most recent call last):
        TypeError: b must be an integer

checking addition of lists
::
        >>> add_integer(1, [])
        Traceback (most recent call last):
        TypeError: b must be an integer
        >>> add_integer([2, 1, 4], [1,2,3])
        Traceback (most recent call last):
        TypeError: a must be an integer

checking addition of dictionarys
::
        >>> add_integer({"add": 3}, float(5))
        Traceback (most recent call last):
        TypeError: a must be an integer

checking addition of boolean values
::
        >>> add_integer(True, 3)
        Traceback (most recent call last):
        TypeError: a must be an integer

checking addition of more then required arguments
::
        >>> add_integer(2, 3, 50)
        Traceback (most recent call last):
        TypeError: add_integer() takes from 1 to 2 positional arguments but 3 were given

checking when no arguments is passed
::
        >>> add_integer()
        Traceback (most recent call last):
        TypeError: add_integer() missing 1 required positional argument: 'a'

::

Test for another data type other than integer:
    >>> add_integer = __import__('0-add_integer').add_integer
    >>> add_integer("hey", 20)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(20, (0,0))
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer


Test if the function takes in float and int:

    >>> add_integer(1.1, 20)
    21

Test for negative number:

    >>> add_integer(-20, 30)
    10



Test if a is empty:

    >> add_integer()
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
