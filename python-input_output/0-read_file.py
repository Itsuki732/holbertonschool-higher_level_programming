#!/usr/bin/python3
"""Module that provides a function to read a text file and print its content"""


def read_file(filename=""):
    """Reads a text file and prints it to standard output"""
    with open(filename, encoding="UTF-8") as file:
        my_file_0 = file.read()
        print(my_file_0, end="")
