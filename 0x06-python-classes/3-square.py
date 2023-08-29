#!/usr/bin/python3
"""Square Class Definition"""


class Square:
    """Representation of a square geometry.

    Attributes:
        side_length (int): Length of the square's side

    """

    def __init__(self, side_length=0):
        """Initialize a Square instance.

        Args:
            side_length (int): Length of the square's side

        Raises:
            TypeError: If side_length is not an integer
            ValueError: If side_length is less than zero

        """
        if not isinstance(side_length, int):
            raise TypeError("side_length must be an integer")
        elif side_length < 0:
            raise ValueError("side_length must be >= 0")
        else:
            self.__side_length = side_length

    def calculate_area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square

        """
        return self.__side_length ** 2
