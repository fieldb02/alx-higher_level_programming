#!/usr/bin/python3
"""Square Class Definition"""


class Square:
    """Representation of a square geometry.

    Attributes:
        side_length (int): Length of the square's side
        position (tuple): Position of the square's top-left corner

    """
    def __init__(self, side_length=0, position=(0, 0)):
        """Initialize a Square instance.

        Args:
            side_length (int, optional): Length of square's side
            position (tuple, optional): Position of the top-left corner

        Raises:
            TypeError: if side_length is not an integer
            ValueError: If side_length is less than zero
            TypeError: if position is not a tuple of two positive integers

        """
        self.side_length = side_length
        self.position = position

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

    @property
    def position(self):
        """Get the position property."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position property."""

        if (
            type(value) is tuple
            and len(value) == 2
            and all(isinstance(p, int) and p >= 0 for p in value)
        ):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def calculate_area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square

        """
        return int(self.side_length) ** 2

    def display(self):
        """Print the square using '#' characters, considering position."""

        if self.side_length > 0:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.side_length):
                print(" " * self.position[0] + "#" * self.side_length)
        else:
            print()
