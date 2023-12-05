#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """
    class_to_json - returns the dictionary description
    with a simple data structure for JSON serialization
    of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: Dictionary description of the object
        with serializable attributes.
    """
    serializable_dict = {}

    # Iterate through object attributes
    for key, value in obj.__dict__.items():
        # Check if the attribute is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict
