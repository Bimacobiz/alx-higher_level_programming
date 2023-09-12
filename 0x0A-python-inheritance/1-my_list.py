#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements printing of the sorted built-in list class."""

    def print_sorted(self):
        """Print a list that has been sorted in ascending order."""
        print(sorted(self))
