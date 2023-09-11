#!/usr/bin/python3
"""Sorting module"""


class MyList(list):
    """list sub-class"""

    def print_sorted(self):
        """prints out the sorted list"""
        print(sorted(self))
