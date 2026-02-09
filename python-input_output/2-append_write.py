#!/usr/bin/python3
"""Module that provides a function to appends a string to a text file"""


def append_write(filename="", text=""):
    """appends a string to a UTF-8 text file and returns number of chars"""
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)
