#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """A representation of base geometry."""

    def area(self):
        """Implementation not done."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validation of a parameter as an integer.

        Args:
            name (str): Parameter name.
            value (int): The parameter that should be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
