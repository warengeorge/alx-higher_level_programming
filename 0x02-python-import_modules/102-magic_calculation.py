#!/usr/bin/python3


def magic_calculation(a, b):
    """
    implement the magic calculation based -
    on a bytcode
    """
    from magic_calculation_102 import add, sub

    if a < b:
        tot = add(a, b)
        for i in range(4, 6):
            tot = add(tot, i)
        return (tot)
    else:
        return (sub(a, b))
