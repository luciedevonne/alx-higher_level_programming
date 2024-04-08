#!/usr/bin/python3
'''creating square class'''


class Square:
    '''defining class'''


    def __init__(self, size=0):
        '''defining object'''

        self.__size = size


    def size(self, value):
        '''setting value'''

         if not isinstance(size, integer):
            raise TypeError('size must be an integer')
        elif size<0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''calculate area'''

        return self.__size = size
