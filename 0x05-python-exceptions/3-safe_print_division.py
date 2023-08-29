#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the redult obtained by dividing a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
