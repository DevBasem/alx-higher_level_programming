#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""


class Node:
    """
    Class that defines properties of a Node.

    Attributes:
        data (int): Data field of the node.
        next_node (Node): Reference to the next node.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): Data for the node.
            next_node (Node): Reference to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data field of the node.

        Returns:
            int: Data field of the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data field of the node.

        Args:
            value (int): New data for the node.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Retrieves the next_node reference.

        Returns:
            Node or None: Reference to the next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node reference.

        Args:
            value (Node or None): Reference to the next node.

        Raises:
            TypeError: If the provided value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Class that defines properties of a SinglyLinkedList.

    Attributes:
        head: Head of the SinglyLinkedList.
    """
    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self._head = None

    def __str__(self):
        """
        Represents the class objects as a string.

        Returns:
            str: String representation of the linked list.
        """
        temp_var = self._head
        print_node = []
        while temp_var:
            print_node.sort()
            print_node.append(str(temp_var.data))
            temp_var = temp_var.next_node

        print_node.sort(key=int)
        return "\n".join(print_node)

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position in the list.

        Args:
            value (int): Value to be inserted.
        """
        if self._head is None:
            new_node = Node(value)
            new_node.next_node = self._head
            self._head = new_node
        else:
            new_node = Node(value)
            new_node.data = value
            new_node.next_node = self._head
            self._head = new_node
