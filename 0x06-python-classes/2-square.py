#!/usr/bin/python3


'''creating class'''


class Square

    def __init__(self, size=0):
        '''initialize instances'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

