#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obtain the dictionary represntation of a student.

        If attrs is a list of strings, on the attributes that are 
        included in a list should be represnted

        Args:
            attrs (list): (Optional) The attributes that should be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replacing all the attributes of student.

        Args:
            json (dict): The key/value pairs  that should be used to replaceattributes.
        """
        for k, v in json.items():
            setattr(self, k, v)
