#!/usr/bin/python3

'''creating class'''


class Square:
    '''Represents a square.'''

    def __init__(self, size=0):
        '''Initializes a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''Calculates and returns the area of the square.'''
        return self.__size ** 2


# Create a Square object with size 3
mysquare = Square(3)

# Print the area of mysquare
print("{}".format(mysquare.area()))  # Output: 9
