#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    module_attributes = dir(hidden_4)
    sorted_attributes = sorted(module_attributes)

    for attribute in sorted_attributes:
        if not attribute.startswith("__"):
            print("{}".format(attribute))

