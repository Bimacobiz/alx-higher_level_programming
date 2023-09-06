#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function."""

# The script starts with the shebang line to specify the Python interpreter.

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    # The function matrix_divided takes two arguments: matrix and div.

    # Check if the matrix argument is a valid matrix (list of lists) containing only
    # integers or floats. If not, raise a TypeError.
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Check if all rows in the matrix have the same size. If not, raise a TypeError.
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if the div argument is a number (int or float). If not, raise a TypeError.
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    # Check if div is 0. If it is, raise a ZeroDivisionError.
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # If all checks pass, perform the division operation using a nested list comprehension.
    # Round the result to two decimal places.
    # Return a new matrix representing the result of the division.
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

