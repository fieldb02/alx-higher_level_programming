#!/usr/bin/python3
"""Defining a Square class"""


class Square:
    """A class representing a square."""

    def __init__(self, side_length):
        """Initialize a Square instance.

        Args:
            side_length (int): Length of the square's side

        """
        self.__side_length = side_length
