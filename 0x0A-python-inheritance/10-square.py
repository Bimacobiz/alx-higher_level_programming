#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square."""

    def __init__(self, size):
        """Initialization of a new square.

        Args:
            size (int): The new square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
