#!/usr/bin/python3
"""
Module that contains a function to return the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Return the dictionary description of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all serializable
        attributes of the object.
    """
    return obj.__dict__
