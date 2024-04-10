#!/usr/bin/python3
'''module defining square'''


class Square:
    '''Instantiation whereby:
    size must be an integer,
    otherwise raise a TypeError exception with the message
    size must be an integer
    if size is less than 0,
    raise a ValueError exception with the message size must be >= 0
    position must be a tuple of 2 positive integer:
    otherwise raise a TypeError
    '''

    def __init__(self, size=0, position(0,0)):
        '''Defining class Square.

        Args:
            size (int): The size of the square. Defaults to 0.
            position of sqaure defaulted to 0,0
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''retrieve position of square'''
        return self.__position

    @size.setter
    '''set position 
    position must be a tuple of 2 positive integers
    '''
    def position(self, value):
        '''position must be a tuple of 2 positive integers
        '''
        if not isinstance(value, len(value) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')

        else:
            self.__position = value

    def area(self):
        '''Calculate the area of the square.'''
        return self.__size ** 2

    def my_print(self):
        '''Print the square using the character '#'.

        If the size is 0, print an empty line.
        position should be use by using space
        '''
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
            for _ in range(self.__position[1]):
                print('' * self.__position[0]
                print('#'* self.__size)

