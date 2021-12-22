#!/usr/bin/python3
""" caching system
    """

BasicCachey = __import__("base_caching").BaseCaching

class FIFOCache(BasicCachey):
    """ caching system:

    Args:
        FIFOCache ([class]): [basic caching]
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        self.cache_data[key] = item
        temp_list = list(self.cache_data.keys())
        if len(temp_list) > self.MAX_ITEMS:
            self.cache_data.pop(temp_list[0])
            print(f"DISCARD: {temp_list[0]}")

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)