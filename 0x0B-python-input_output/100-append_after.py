#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting a text after each line that are contained in a given string
     in a file.

    Args:
        filename (str): The file's name.
        search_string (str): The string that should be
        searched withing the file.
        new_string (str): String that should be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
