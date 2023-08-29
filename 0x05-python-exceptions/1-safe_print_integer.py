#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer that has the "{:d}".format().

    Args:
        value (int): integer to be printed.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))  # Try to format and print the integer
        return True
    except (TypeError, ValueError):
        return False  # Handle the exception by returning False
