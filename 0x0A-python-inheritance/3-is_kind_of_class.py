#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checking if an object is an instance or if it is an inherited instance of a class.

    Args:
        obj (any): The object that should be checked.
        a_class (type): The class to which the type of obj should be matched.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
