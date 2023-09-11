#!/usr/bin/python3
"""My module"""


def is_kind_of_class(obj, a_class):
    """checks whether an obkject is exactly same/inherited
    Args:i
         obj(any) = Object to be checked
         a_class(type) = Class to match the type with
    Return:
           True if object is exactly an instance, else, 
           False
    """
    if isinstance(obj, a_class):
        return True
    return False
