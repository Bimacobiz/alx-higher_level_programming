#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of a rectange using BaseGeometry."""

    def __init__(self, width, height):
        """Initialization of a new Rectangle.

        Args:
            width (int): The rectangle width.
            height (int): Rectangle Height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
