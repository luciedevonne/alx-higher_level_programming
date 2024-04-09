#!/usr/bin/python3
'''module defining class Square'''


class Square:
    '''Instantiation whereby:
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    '''

    def __init__(self, size=0):
        '''defining class Square,
        meant to have this in class Square
        '''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    '''retrieveing size
    '''

    def size(self):
        return self.__size

    @size.setter
    '''setting size
    '''

    def size(self, value):
        if not isinstance(value, integer):
            raise TypeError('size must be an integer')
        elif size<0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        '''defining srea
        '''

        return (self.__size ** 2)

    def my_print(self):
        '''printing out the sqaure using the character
        '''

        if self.__size == 0:
            print()

        else:
            for _ in range(self.__size):
                print('#' * self.__size)

