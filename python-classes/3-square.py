#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
