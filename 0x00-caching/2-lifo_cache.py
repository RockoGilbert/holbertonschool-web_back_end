#!/usr/bin/python3
""" BaseCaching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache system"""

    def __init__(self):
        """Initialize the LIFO cache"""
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        """Add a key to the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.current_keys:
                self.current_keys.append(key)
            else:
                self.current_keys.append(
                    self.current_keys.pop(self.current_keys.index(key)))
            if len(self.current_keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.current_keys.pop(-2)
                del self.cache_data[discarded_key]

    def get(self, key):
        """Get an item by the key"""
        return self.cache_data[key]
