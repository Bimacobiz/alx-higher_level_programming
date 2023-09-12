#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obtain the dictionary rep of the student.

        If attrs is a list of strings, it represents the 
        attributes that a list contains.

        Args:
            attrs (list): (Optional) attributes that should be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
