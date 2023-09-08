#!/usr/bin/python3
# 3-say_my_name.py
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The name that will be printed first.
        last_name (str): The name that will be printed last.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """

    # The function say_my_name takes two arguments: first_name and last_name.
    # The last_name argument is optional and defaults to an empty string.

    # Check if first_name is a string. If not, raise a TypeError.
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string. If not, raise a TypeError.
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # If both first_name and last_name are strings, print the formatted name.
    print("My name is {} {}".format(first_name, last_name))
