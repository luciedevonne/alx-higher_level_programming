#!/usr/bin/python3

'''create class Square'''


class Square:
    '''initialize instances of square'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size<0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''calculate area of square'''
        return self.__size **2
