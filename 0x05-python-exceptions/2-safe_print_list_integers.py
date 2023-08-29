#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements that are contained in a list that are integers.

    Args:
        my_list (list): The list from which the elements should be printed.
        x (int): The number of elements contained in my_list that should be printed.

    Returns:
        The number of printed elements.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
