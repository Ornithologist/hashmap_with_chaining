from types import *

class Hashmap(object):

    def __init__(self, size):
        self.size = size
        self.count = 0
    
    def set(self, key, value):
        return True

    def get(self, key):
        return None

    def delete(self, key):
        return True

    def load(self):
        return float (self.count) / self.size
