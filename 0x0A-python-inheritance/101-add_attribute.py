#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Addition of a new attribute to an object if possible.

    Args:
        obj (any): The object to which the attribute should be added.
        att (str): The name of the attributes that should be added to the obj.
        value (any): The value of att.
    Raises:
        TypeError: If the addition of the object fails.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
