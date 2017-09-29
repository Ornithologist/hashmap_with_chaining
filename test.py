from __future__ import division

import unittest2
from hashmap import Hashmap


class Test(unittest2.TestCase):

    def test_constructor(self):
        print "Testing constructor with size equal to 10"
        # test normal creation
        my_hash_table = Hashmap(10)
        self.assertIsInstance(my_hash_table, Hashmap)
        print "Testing constructor with size value 'bad input'"
        # test erroneous creation
        with self.assertRaises(TypeError) as cm:
            my_hash_table = Hashmap("bad input")

        self.assertEqual(cm.exception.message,
                         "size must be a positive integer.")
        print "Test passed"

    def test_set(self):
        my_hash_table = Hashmap(3)
        print "Testing set with key 'foo', and value 'bar'"
        # test single call of set        
        self.assertTrue(my_hash_table.set("foo", "bar"))
        print "Testing set with integer key 123, and value 123"
        # test erroneous set
        with self.assertRaises(TypeError) as cm:
            my_hash_table.set(123, 123)

        self.assertEqual(cm.exception.message,
                         "key must be a string.")
        print "Testing set with key 'foo2', and value 'bar2'"
        # test second call of set
        self.assertTrue(my_hash_table.set("foo2", "bar2"))
        print "Testing set with key 'foo3', and value 'bar3'"
        # test for collision with "foo" on 64bit system
        self.assertTrue(my_hash_table.set("foo3", "bar3"))
        print "Testing over-sized set"
        # test size check
        self.assertFalse(my_hash_table.set("foo4", "bar4"))
        print "Test passed"

    def test_get(self):
        my_hash_table = Hashmap(3)
        my_hash_table.set("foo", "bar")
        my_hash_table.set("foo2", 2)
        my_hash_table.set("foo3", 3)
        print "Testing get with non-existing key"
        # test non-existing key
        self.assertIsNone(my_hash_table.get("foo4"))
        print "Testing get with key 'foo'; value is 'bar'"
        # test first get
        self.assertEqual(my_hash_table.get("foo"), "bar")
        print "Testing get with key 'foo2'; value is 2"
        # test second get
        self.assertEqual(my_hash_table.get("foo2"), 2)
        print "Testing get with key 'foo3'; value is 3"
        # test thrid get with collision key on 64bit system
        self.assertEqual(my_hash_table.get("foo3"), 3)
        print "Test passed"        

    def test_delete(self):
        my_hash_table = Hashmap(3)
        my_hash_table.set("foo", "bar")
        print "Testing delete with non-existing key"
        # test non-existing key
        self.assertIsNone(my_hash_table.delete("foo2"))
        print "Testing delete with key 'foo'; value is 'bar'"
        # test first and only delete
        self.assertEqual(my_hash_table.delete("foo"), "bar")
        print "Testing delete with previously removed key 'foo'"
        # test if above delete worked
        self.assertIsNone(my_hash_table.delete("foo"))
        print "Test passed"        

    def test_load(self):
        my_hash_table = Hashmap(3)
        my_hash_table.set("foo", "bar")
        my_hash_table.set("foo2", 2)
        my_hash_table.set("foo3", 3)
        print "Testing load, expected load factor to be 0.75"
        # test if load factor is 3 / 4
        self.assertEqual(my_hash_table.load(), 3 / 4)
        print "Test passed"
    
if __name__ == "__main__":
    unittest2.main()