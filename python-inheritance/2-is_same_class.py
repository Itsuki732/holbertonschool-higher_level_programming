#!/usr/bin/python3
"""Module that difine a function to check class type"""
def is_same_class(obj, a_class):
    """Return True if obj is exactly a instence of a_class"""
    return type(obj) is a_class
