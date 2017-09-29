'''
    Hashmap
    An implementation of fixed-size hashmap based on Python primitive types
    and separate chaining. Heavily inspired by MIT opencourseware and
    Java's Hashmap implementation.

    Example:
        from hashmap from Hashmap
        my_hash_table = Hashmap(15)
        my_hash_table.set("foo", "bar")
        bar = my_hash_table.get("foo")      # "bar"
        my_hash_table.set("foo", "hoe")
        hoe = my_hash_table.delete("foo")   # "hoe"
        load_factor = my_hash_table.load()  #
'''
from __future__ import division


class Hashmap(object):
    '''

    '''

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
        if self.count == self.size:
            return False
        bucket_idx, node_idx = self.__search(key)
        if node_idx:
            self.table[bucket_idx][node_idx] = (key, value)  # overwrite
        else:
            self.table[bucket_idx].append((key, value))  # add new value
        self.count += 1
        return True

    def get(self, key):
        bucket_idx, node_idx = self.__search(key)
        if node_idx is None:
            return None
        return self.table[bucket_idx][node_idx][1]

    def delete(self, key):
        bucket_idx, node_idx = self.__search(key)
        if node_idx is None:
            return None
        value = self.table[bucket_idx][node_idx][1]
        del self.table[bucket_idx][node_idx]
        self.count -= 1
        return value

    def load(self):
        return self.count / self.capacity
