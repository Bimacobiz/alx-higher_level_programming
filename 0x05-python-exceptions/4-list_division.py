#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """A function that divides element by element 2 lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): the number of elements that should be divided.

    Returns:
        A new list of list_length that contains the divisions done.
    """
    new_list = []  # Initialize an empty list to store the division results
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]  # Attempt to perform division
        except TypeError:
            print("wrong type")  # Handle TypeError by printing an error message
            div = 0
        except IndexError:
            print("out of range")  # Handle IndexError by printing an error message
            div = 0
	except ZeroDivisionError:
            print("division by 0")  # Handle ZeroDivisionError by printing an error message
            div = 0
        finally:
            new_list.append(div)  # Append the division result to the new list
    return new_list  # Return the list of division results
