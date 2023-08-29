#!/usr/bin/python3
"""Definition of classes belonging to a singly-linked list."""


class Node:
    """Representation of a given node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialization of a new node.

        Args:
            data (int): data to be added to the new node.
            next_node (Node): the next node after the new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Geting or settng data of the node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A representation of a singly-linked list."""

    def __init__(self):
        """Initalization of a SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserting the new node created into the SinglyLinkedList.

        It must be added at the correct numerical position.

        Args:
            value (Node): The new node that should be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Definition of the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
