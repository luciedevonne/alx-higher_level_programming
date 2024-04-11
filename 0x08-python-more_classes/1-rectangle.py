#!/usr/bin/python3
"""Empty class Rectangle that defines a rectangle."""


class Rectangle:
    """Empty class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
       '''set the value of the rectangle
        
        Args:
        value(int): the size value to be set

        Raises:
        TypeError if width is not an integer
        ValueError if width is less than 0
        '''
        if width < 0:
            raise ValueError('width must be >= 0')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__width = width
        self.__height = height
        
    @property
    def width(self):
        '''retrieves the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the value of the rectangle
        
        Args:
        value(int): the size value to be set

        Raises:
        TypeError if width is not an integer
        ValueError if width is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        
        self.__width = value

    @property
    def height(self):
        '''retrieves the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setting the height  of the rectangle
        
        Args:
        value(int): the height value to be set

        Raises:
        TypeError if height is not an integer
        ValueError if height is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        
        self.__height = value
