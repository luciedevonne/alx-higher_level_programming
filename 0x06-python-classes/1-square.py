#!/usr/bin/python3


class Square:

    """creating instances of class"""

    def __init__(self, size):
        self.__size = size


square = Square(5)
print("Size: ", square._Square__size)
