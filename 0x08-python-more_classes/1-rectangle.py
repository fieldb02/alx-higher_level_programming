#!/usr/bin/python3
"""Defining a rectangle"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter - Finds the value of width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter- setting the value of width
            Args:
                value(int): Value to set of width
            """

            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise TypeError("width must be >= 0")

            self.__width = value

        @property
        def height(self):
            """Getter - Finds the value of height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter- Setting value of height
           Args:
                value(int): Sets value of the height
            """

            if type(value) != int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise TypeError("height must be >= 0")

            self.__height = value
