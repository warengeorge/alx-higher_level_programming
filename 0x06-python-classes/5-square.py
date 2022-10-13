#!/usr/bin/python3
""" Square module """


class Square:
    """ defines a square class """

    def __init__(self, size=0) -> None:
        """
        Intialize the attributes
        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """ defines a getter for size attributes """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ computes the area of a square """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            count = 0
            while count < self.__size:
                num = 0
                while num < self.__size:
                    print("{}".format("#"), end='')
                    num += 1
                print()
                count += 1
