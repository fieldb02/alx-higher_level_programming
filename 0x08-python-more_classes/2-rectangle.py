#!/usr/bin/python3
'''Defining a rectangle'''


class Rectangle:
    '''Classing a regtangle'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    '''attribute:
        width(int): width of rectangle
        height(int): heightof rectangle
    '''
    '''retrieving width'''
    @property
    def width(self):
        return self.__width

    '''setting width'''
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    '''retrieving height'''
    @property
    def height(self):
        return self.__height

    '''setting height'''
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    '''area of rectangle'''
    def area(self):
        return self.__width * self.__height

    '''perimeter of rectangle'''
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
