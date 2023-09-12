#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checking if the object is exactly an instance of the given class.

    Args:
        obj (any): The object that should be checked.
        a_class (type): The class to which the obj should be matched.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
