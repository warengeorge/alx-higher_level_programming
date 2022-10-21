#!/usr/bin/python3
"""
    2-matrix_divided Module
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix
        Args:
            matrix: intial 2D list
            div: integer which is the divisor
        Returns:
            New matrix containing the divided elements
            rounded to 2 decimal places
    """
    _len = 0
    _message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(_message)

    for m in matrix:    # matrix is a list
        if type(m) is not list:
            raise TypeError(_message)

        for el in m:
            if type(el) is not int and type(el) is not float:
                raise TypeError(_message)

        if len(m) != _len and _len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        _len = len(m)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
