#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Empty geometry module"""
    def area(self):
        """showing the error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Det value

        Args:
            name(str)= Name of paramter
            value(int) = Parameter to Det"
        Return:
               TypeError = if the value is not int
                ValueError = if the value is less than zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
