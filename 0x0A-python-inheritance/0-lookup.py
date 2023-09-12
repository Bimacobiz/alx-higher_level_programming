#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list that contains the object's available attributes."""
    return (dir(obj))
