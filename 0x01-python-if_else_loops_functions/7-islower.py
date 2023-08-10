#!/usr/bin/python3
# 7-islower.py


def islower(c):
    """Check lowercase chars."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
