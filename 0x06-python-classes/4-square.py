#!/usr/bin/python3
'''Defines a Square class'''

class Square:
    '''Represents a square'''


    def __init__(self, size=0):
        '''Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.
        '''
        self.__size = size

    def size(self, value):
        '''Sets the size of the square.

        Args:
            value (int): The size to set for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''Calculates the area of the square.

        Returns:
            int: The area of the square.
        '''
        return self.__size ** 2
