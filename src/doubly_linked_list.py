"""This module contains DoublyLinkedList and Node class."""
from src.exceptions import DoublyLinkedListError


class Node:
    """This class contain methods related to creating, updating nodes used in DoublyLinkedList."""
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None

    def update_next(self, next_node=None):
        """
        This method updates the next node of the current node.
        :param next_node: Node
        :return: None
        """
        self.next_node = next_node

    def update_previous(self, previous_node=None):
        """
        This method updates the previous node of the current node.
        :param previous_node: Node
        :return:  None
        """
        self.previous_node = previous_node


class DoublyLinkedList:
    """This class contains methods related to creating a DoublyLinkedList used in creating a MRU Cache."""
    def __init__(self):
        self._header = None
        self._tail = None

    def append(self, value):
        """
        This method appends a node at the tail of the DoublyLinkedList.
        :param value: str
        :return: None
        """
        node = Node(value)

        if not self._header and not self._tail:
            self._header = node
            self._tail = node
        else:
            node.update_previous(self._tail)
            self._tail.update_next(node)
            self._tail = node

    def insert_at_head(self, value):
        """
        This method inserts a node at the head of the DoublyLinkedList.
        :param value: str
        :return: None
        """
        node = Node(value)

        if not self._header and not self._tail:
            self._header = node
            self._tail = node
        else:
            node.update_next(self._header)
            self._header.update_previous(node)
            self._header = node

    def pop(self):
        """
        This method pops a node from the tail of the DoublyLinkedList.
        :return: str
        """
        if not self._tail:
            raise DoublyLinkedListError("Empty linkedlist.")

        popped_node = self._tail

        if self._header == self._tail:
            self._header = None
            self._tail = None
        else:
            self._tail = popped_node.previous_node
            self._tail.update_next()

        popped_node.update_previous()
        return popped_node.value

    def remove_from_head(self):
        """
        This method removes a node from the head of the DoublyLinkedList.
        :return: str
        """
        if not self._header:
            raise DoublyLinkedListError("Empty linkedlist.")

        popped_node = self._header

        if self._header == self._tail:
            self._header = None
            self._tail = None
        else:
            self._header = popped_node.next_node
            self._header.update_previous()

        popped_node.update_next()
        return popped_node.value

    def remove_value(self, value):
        """
        This method removes a node based on the value from within the DoublyLinkedList.
        :param value: str
        :return: None
        """
        if not self._header:
            raise DoublyLinkedListError("Empty linkedlist.")

        popped_node = None
        node = self._header
        while node:
            if node.value == value:
                popped_node = node
                break
            node = node.next_node

        if not popped_node:
            raise DoublyLinkedListError("Value not found.")

        if not popped_node.next_node:
            self.pop()
            return

        if not popped_node.previous_node:
            self.remove_from_head()
            return

        prev_node = popped_node.previous_node
        next_node = popped_node.next_node
        prev_node.update_next(next_node)
        next_node.update_previous(prev_node)

    def get_list(self):
        """
        This method prints the DoublyLinkList .
        :return: list
        """
        node = self._header
        output = []

        while node:
            output.append(node.value)
            node = node.next_node

        return output

    def get_header(self):
        """
        This method returns current header of the DoublyLinkedList.
        :return: Node
        """
        return self._header
