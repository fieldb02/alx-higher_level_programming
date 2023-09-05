#!/usr/bin/python3
'''Def a rectangle'''


class Rectangle:
    '''Class of rectangle created'''
    number_of_instances = 0
    print_symbol = '#'

    '''initializing a regtangle'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1
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

    '''print area as #'''
    def pr_st(self):
        if self.__width == 0:
            return ''
        else:
            return '\n'.join(
                str(self.print_symbol) * self.__width
                for i in range(self.__height))

    '''return area as a str(#)'''
    def __str__(self):
        return f"{self.pr_st()}"

    '''return area as string representation...to recreate a new instance'''
    def __repr__(self):
        return f"Rectangle{self.__width, self.__height}"

    '''deleting a rectangle'''
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    '''static method'''
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
