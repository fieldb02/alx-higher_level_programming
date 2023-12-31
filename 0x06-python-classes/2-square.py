#!/usr/bin/python3
"""Defining a new square"""


class Square:
    """creating a new square."""

    def __init__(self, size=0):
        """creating new square.
        Args:
            size (int): Size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
