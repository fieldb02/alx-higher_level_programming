#!/usr/bin/python3
"""My module"""


def inherits_from(obj, a_class):
    """checks whether if inherited instance
      of class
    Args:
         obj(any) = Object to be checked
         a_class(type) = Class to match type with
    Return:
           True if object is exactly an instance, else,
           False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
