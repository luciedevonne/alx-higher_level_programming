#!/usr/bin/python3
'''module defining square'''


class Square:
    '''Instantiation whereby:
    size must be an integer,
    otherwise raise a TypeError exception with the message
    size must be an integer
    if size is less than 0,
    raise a ValueError exception with the message size must be >= 0
    '''

    def __init__(self, size=0):
        '''Defining class Square.

        Args:
            size (int): The size of the square. Defaults to 0.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        '''Retrieve the size of the square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the size of the square.

        Args:
            value (int): The size value to be set.

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
        '''Calculate the area of the square.'''
        return self.__size ** 2

    def my_print(self):
        '''Print the square using the character '#'.

        If the size is 0, print an empty line.
        '''
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
