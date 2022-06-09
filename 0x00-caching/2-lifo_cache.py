#!/usr/bin/python3

"""
Module for LIFO Caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
     inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.all_keys = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            to_discard = self.all_keys.pop()
            print("DISCARD: {}".format(to_discard))
            del self.cache_data[to_discard]

        self.all_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
