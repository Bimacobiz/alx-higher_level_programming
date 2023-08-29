#!/usr/bin/python3
"""Definition of a class Square."""


class Square:
    """Representation of a square."""

    def __init__(self, size):
        """Initialization of a new square.

        Args:
            size (int): the new square size.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the square size (current)."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the current square created."""
        return (self.__size * self.__size)

    def my_print(self):
        """Printing the square and include the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
