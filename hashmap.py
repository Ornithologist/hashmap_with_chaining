from types import *

class Hashmap(object):

    def __init__(self, size):
        if not isinstance(size, int) or size <= 0:
            raise TypeError("size must be a positive integer.")
        capacity = 1
        while capacity < size:
            capacity <<= 1
        self.table = [[]] * capacity
        self.capacity = capacity
        self.size = size
        self.count = 0

    def __idx__(self, key):
        if not isinstance(key, basestring):
            raise TypeError("key must be a string.")
        return key.__hash__() & (self.capacity - 1)

    def __search(self, key):
        node_idx = None
        idx = self.__idx__(key)
        bucket = self.table[idx]
        for i, node in enumerate(bucket):
            if node[0] == key:
                node_idx = i
                break
        return idx, node_idx

    def set(self, key, value):
        bucket_idx, node_idx = self.__search(key)
        self.table[bucket_idx][node_idx] = (key, value)
        return True

    def get(self, key):
        bucket_idx, node_idx = self.__search(key)
        if node_idx is None:
            return None
        return self.table[bucket_idx][node_idx]

    def delete(self, key):
        bucket_idx, node_idx = self.__search(key)
        if node_idx is None:
            return None
        value = self.table[bucket_idx][node_idx]
        del self.table[bucket_idx][node_idx]
        return value

    def load(self):
        return float(self.count) / self.capacity
