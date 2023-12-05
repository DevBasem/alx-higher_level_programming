#!/usr/bin/python3
"""student module"""


class Student:
    """
    Student class definition.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with
        first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of strings specifying attributes to retrieve.
                          If None, retrieve all attributes.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            # If attrs is None or not a list, retrieve all attributes
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }

        # Retrieve only the specified attributes in attrs
        return {
            attr: getattr(self, attr)
            for attr in attrs
            if hasattr(self, attr)
        }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with
        values from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
