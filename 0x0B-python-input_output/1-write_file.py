#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Writing a string to UTF8 text file.

    Args:
        filename (str): The name of the file that should be written.
        text (str): The text that should be written to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
