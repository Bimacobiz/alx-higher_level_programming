#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    elements_to_print = my_list[:x]  # Use list slicing to get the elements to print
    for element in elements_to_print:
        print("{}".format(element), end="")
    print("")  # Print a newline after printing the elements
    return len(elements_to_print)  # Return the number of elements actually printed
