#!/usr/bin/python3
# 0-add_integer.py
"""Defines a function that will add an integer."""


def add_integer(a, b=98):
    """Return the result of a + b's integer addition.

    Prior to addition, float arguments are typecast to ints.

    Raises:
        TypeError: In the event that either an or b is not an
        integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
    
# Test cases
    try:
        result = add_integer(3, 5)
        print(result)  # This should print 8

        result = add_integer(3.5, 5.2)
        print(result)  # This should print 8

        result = add_integer(3)
        print(result)  # This should print 101 (3 + 98)
    except TypeError as e:
        print("Error:", e)
