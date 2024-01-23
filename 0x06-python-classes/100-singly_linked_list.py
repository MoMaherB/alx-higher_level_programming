#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""


class Node:
    """Class that create node"""
    def __init__(self, data, next_node=None):
        """instances of node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data field instance."""
        return self.__data

    @data.setter
    def data(self, value):
        """Propery setter for data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns: The next_node instance."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines properties of SinglyLL"""
    def __init__(self):
        """new instances of SinglyLinkedList"""
        self.__head = None

    def __str__(self):
        """class objects as a string."""
        temp_var = self.__head
        print_node = []
        while temp_var:
            print_node.sort()
            print_node.append(str(temp_var.data))
            temp_var = temp_var.next_node

        print_node.sort(key=int)
        return ("\n".join(print_node))

    def sorted_insert(self, value):
        """Inserts a new node at a given position."""
        if self.__head is None:
            new_node = Node(value)
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node = Node(value)
            new_node.data = value
            new_node.next_node = self.__head
            self.__head = new_node
