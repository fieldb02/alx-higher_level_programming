#!/usr/bin/python3
"""Module"""


def is_same_class(obj, a_class):
    """Checks whether object is exactly the same

    Args:
         obj(any) = Object to check
         a_class(type) = Class to match type with
    Return:
           True if object is exactly an instance, else,
           False
    """
    if type(obj) == a_class:
        return True
    return False
