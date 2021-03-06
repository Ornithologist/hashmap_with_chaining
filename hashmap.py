'''
    Hashmap
    An implementation of fixed-size hashmap based on Python primitive types
    and separate chaining. Heavily inspired by MIT opencourseware and
    Java's Hashmap implementation.

    Example:
        from hashmap import Hashmap
        my_hash_table = Hashmap(15)
        my_hash_table.set("foo", "bar")
        my_hash_table.set("foo2", "bar2")
        bar = my_hash_table.get("foo")      # "bar"
        my_hash_table.set("foo", "hoe")
        hoe = my_hash_table.delete("foo")   # "hoe"
        load_factor = my_hash_table.load()  # 0.0625
'''
from __future__ import division


class Hashmap(object):
    def __init__(self, size):
        """
            @param size: number of (key, value) pairs it can accept
            @return: an instance of Hashmap
        """
        if not isinstance(size, int) or size <= 0:
            raise TypeError("size must be a positive integer.")
        capacity = 1
        while capacity < size:
            capacity <<= 1
        self.table = [[]] * capacity  # hashmap content
        self.capacity = capacity  # number of buckets it has
        self.size = size  # user defined size
        self.count = 0  # number of (key, value) pairs it has

    def __idx__(self, key):
        """
            @param key: string provided to identify the value
            @return: prehashed integer generated using the key
        """
        if not isinstance(key, basestring):
            raise TypeError("key must be a string.")
        return key.__hash__() & (self.capacity - 1)

    def __search(self, key):
        """
            @param key: string provided to identify the value
            @return idx: prehashed integer generated using the key
            @return node_idx: the index of the n-th node that contains the key
        """
        node_idx = None
        idx = self.__idx__(key)
        bucket = self.table[idx]
        for i, node in enumerate(bucket):
            if node[0] == key:
                node_idx = i
                break
        return idx, node_idx

    def set(self, key, value):
        """
            @param key: string provided to identify the value
            @param value: value to be stored
            @return (bool): True if set successfully, False if hashmap is full
        """
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
        """
            @param key: string provided to identify the value
            @return: None if not found, else return the value
        """
        bucket_idx, node_idx = self.__search(key)
        if node_idx is None:
            return None
        return self.table[bucket_idx][node_idx][1]

    def delete(self, key):
        """
            @param key: string provided to identify the value
            @return: None if not found, else return the value
            Removes the (key, value) pair from the bucket
        """
        bucket_idx, node_idx = self.__search(key)
        if node_idx is None:
            return None
        value = self.table[bucket_idx][node_idx][1]
        del self.table[bucket_idx][node_idx]
        self.count -= 1
        return value

    def load(self):
        """
            @return: load factor = number of (key, value) pairs / capacity
        """
        return self.count / self.capacity
