#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    """Defines a student by first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list): List of attributes to retrieve

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

        return self.__dict__
