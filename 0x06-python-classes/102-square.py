#!/usr/bin/python3
"""Definition of a new square."""


class Square:
    """Representign the defined square."""

    def __init__(self, size=0):
        """Initializing the defined new square.

        Args:
            size (int): the new square size.
        """
        self.size = size

    @property
    def size(self):
        """Geting/seting the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the current square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Definition of the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Definition of the != comparison to the given Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Definition of the < comparison to a given square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Definition of the <= comparison to the given Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Definition of the > comparison to the given Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Definition of the >= compmarison to the given Square."""
        return self.area() >= other.area()
