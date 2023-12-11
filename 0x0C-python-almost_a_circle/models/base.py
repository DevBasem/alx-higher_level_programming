#!/usr/bin/python3
""" Base Module """
import json


class Base:
    """ Base class for managing id attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method to convert list of dictionaries to JSON string """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method to save JSON string representation
        of list_objs to a file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"

        # Convert instances to dictionaries
        dictionaries = [obj.to_dictionary() for obj in list_objs]

        # Convert dictionaries to JSON string
        json_string = cls.to_json_string(dictionaries)

        # Write JSON string to file
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Static method to convert JSON string to list of dictionaries """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method to create instance with attributes
        set from dictionary """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ Class method to return a list of instances from a file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [
                    cls.create(**dictionary)
                    for dictionary in dictionaries
                    ]
                return instances
        except FileNotFoundError:
            return []
