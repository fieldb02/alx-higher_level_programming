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
            side_length (int, optional): Length of square's side

        Raises:
             TypeError: if side_length is not an integer
             ValueError: If side_length is less than zero

         """
        self.side_length = side_length

    @property
    def side_length(self):
        """Get the side length property.

        Returns:
            int: side_length
        """
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        """Set the side length property."""

        if not isinstance(value, int):
            raise TypeError("side_length must be an integer")
        elif value < 0:
            raise ValueError("side_length must be >= 0")
        else:
            self.__side_length = value

    def calculate_area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square

        """
        return int(self.side_length) ** 2

    def display(self):
        """Prints the square using '#' characters."""

        if self.side_length > 0:
            for _ in range(self.side_length):
                print("#" * self.side_length)
        else:
            print()
