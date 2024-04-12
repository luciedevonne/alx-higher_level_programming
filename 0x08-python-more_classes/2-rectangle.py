#!/usr/bin/python3
'''module defining rectangle'''


class Rectangle:
    '''defines a rectangle by: (based on 0-rectangle.py)'''
    def __init__(self, width=0, height=0):
        '''Initialize a Rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If width or height is less than 0.
        '''
        if width < 0:
            raise ValueError('width must be >= 0')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Retrieve the width of the rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of the rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Retrieve the height of the rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height of the rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


    def area(self):
        '''return area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''return perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__width * 2) + (self.__height * 2)
