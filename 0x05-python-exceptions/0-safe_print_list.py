#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """The function will print x elememts of a given list.

    Args:
        my_list (list): List provided from which to print elements.
        x (int): The number of elements contained in my_list to print.

    Returns:
        The number of elements that have been printed.
    """
    ret = 0  # Initialize a variable to keep track of the printed elements
    for i in range(x):
        try:
            # Try to print the i-th element of the list
            print("{}".format(my_list[i]), end="")
            ret += 1  # Increment the counter of printed elements
        except IndexError:
            # Handle the case when the index is out of bounds
            break  # Exit the loop if an IndexError occurs (no more elements to print)
    print("")  # Print a newline after printing the elements
    return ret  # Return the number of elements actually printed
