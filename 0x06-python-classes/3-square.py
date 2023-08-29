#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represention of a square."""

    def __init__(self, size=0):
        """Initialize a square instance.
        Args:
            size (int): Length of square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate area of square."""
        return (self.__size * self.__size)
