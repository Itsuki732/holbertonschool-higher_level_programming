#!/usr/bin/python3
"""Module that provides a function to write a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns number of chars"""
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
