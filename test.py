import unittest2
from hashmap import Hashmap


class Test(unittest2.TestCase):

    def test_constructor(self):
        # test normal creation
        my_hash_table = Hashmap(10)
        self.assertIsInstance(my_hash_table, Hashmap)
        # test erroneous creation
        with self.assertRaises(TypeError) as cm:
            my_hash_table = Hashmap("bad input")

        self.assertEqual(cm.exception.message,
                         "size must be a positive integer.")

    def test_set(self):
        # test single call of set
        my_hash_table = Hashmap(3)
        self.assertTrue(my_hash_table.set("foo", "bar"))
        # test second call of set
        self.assertTrue(my_hash_table.set("foo2", "bar2"))
        # test for collision with "foo"
        self.assertTrue(my_hash_table.set("foo3", "bar3"))
        # test size check
        self.assertFalse(my_hash_table.set("foo4", "bar4"))
        return True

    def test_get(self):
        my_hash_table = Hashmap(3)
        my_hash_table.set("foo", "bar")
        my_hash_table.set("foo2", 2)
        my_hash_table.set("foo3", 3)
        # test non-existing key
        self.assertIsNone("foo4")
        # test first get
        self.assertEqual(my_hash_table.get("foo"), "bar")
        # test second get
        self.assertEqual(my_hash_table.get("foo2"), 2)
        # test thrid get with collision key
        self.assertEqual(my_hash_table.get("foo3"), 3)
        return True

    def test_delete(self):
        my_hash_table = Hashmap(3)
        my_hash_table.set("foo", "bar")
        # test non-existing key
        self.assertIsNone(my_hash_table.delete("foo2"))
        # test first and only delete
        self.assertEqual(my_hash_table.delete("foo"), "bar")
        # test if above delete worked
        self.assertIsNone(my_hash_table.delete("foo"))

    def test_load(self):
        my_hash_table = Hashmap(3)
        my_hash_table.set("foo", "bar")
        my_hash_table.set("foo2", 2)
        my_hash_table.set("foo3", 3)
        # test if load factor is 3 / 4
        self.assertEqual(my_hash_table.load(), 3 / 4)
    
if __name__ == "__main__":
    unittest2.main()