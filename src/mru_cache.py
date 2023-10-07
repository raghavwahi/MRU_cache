"""This module contains MRU class."""
from src.doubly_linked_list import DoublyLinkedList
from src.exceptions import DoublyLinkedListError


class MRUCache:
    """This class contains methods to utilize an MRU cache."""
    def __init__(self, capacity):
        self.capacity = capacity
        self._current_filled = 0
        self._data = {}
        self._list = DoublyLinkedList()

    def put(self, key, value):
        """
        This method updates cache with the added key, value pair.
        :param key: str
        :param value: dict
        :return: None
        """
        if not self._current_filled:
            self._list.insert_at_head(key)
            self._data[key] = value
            self._current_filled += 1
        else:
            if self._list.get_header().value == key:
                return
            try:
                self._list.remove_value(key)
                self._list.insert_at_head(key)
            except DoublyLinkedListError as error:
                if self._current_filled < self.capacity:
                    self._list.insert_at_head(key)
                    self._data[key] = value
                    self._current_filled += 1
                elif self._current_filled == self.capacity:
                    popped_key = self._list.pop()
                    del self._data[popped_key]
                    self._list.insert_at_head(key)
                    self._data[key] = value

    def get(self, key):
        """
        This method returns the cached dict based on the key
        :param key: str
        :return: dict
        """
        try:
            self._list.remove_value(key)
        except DoublyLinkedListError:
            raise KeyError(key)

        self._list.insert_at_head(key)
        return {**self._data[key]}

    def get_cache(self):
        """
        This method returns the current cache state.
        :return: dict
        """
        return {key: {**value} for key, value in self._data.items()}
