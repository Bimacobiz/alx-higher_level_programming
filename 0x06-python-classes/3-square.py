#!/usr/bin/python3
"""Definition of a square"""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Initialization of a new square.

        Args:
            size (int): the new square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
