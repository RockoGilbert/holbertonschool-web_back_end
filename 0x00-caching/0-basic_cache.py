#!/usr/bin/python3
"""Basic cache class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache class

    Args:
    BaseCaching (class): Basic cache class
    """

    def put(self, key, item):
        """Put a key/value pair into cache
        Args:
            key ([type]): Key/value pair
            item (type): Key/value pair
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get a key/value pair from cache
        Args
            key (str): Key/value pair
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
