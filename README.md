# hashmap_with_chaining
A fixed-size hashmap using only primitive Python data types.

## Basic
An implementation of fixed-size hashmap based on Python primitive types, built-in hash function[1](#references), and separate chaining -- heavily inspired by MIT opencourseware[2](#references) and Java's Hashmap implementation[3](#references).

The internal data structure carrying the information of the _Hashmap_ is an array varialbe called _table_. _Hashmap_ prehashes argument _key_ given by user with Python's built-in hash function[1](#references) into an numeric value. It then hashes this value using a simple hash function (see below) to get the _idx_ of the slot to be inserted into _table_. _table_ has length equals to _capacity_.

### Sizing
The _capacity_ of the hashmap is determined using the user-passed-in argument _size_. More specifically, _capacity_ is the smallest power of 2 that is bigger than or equal to _size_.

Such implementation avoids initiating unnecessarily large _table_. Meantime it controls the collision rate to make search faster.

### Hashing and Chaining
Prehashing is done using Python's built-in hash function[1](#references) to convert string _key_ to integer. _Hashmap_ then convert this integer to the final hash value _idx_ by `integer_value mod capacity`. _idx_ is used later-on to insert the (_key_, _value_) pair to _table_.

We use separate chaining to solve collision. When _key_ *foo* and "foo3* collide with each other, we append *foo3* to the list where *foo* was inserted to. _table_ maintains _capcity_ number of such lists.

## How to Use

### Build
To build, use:
```
make hashmap.pyc
```
to compile the pyc file for external usage.

You may want to run:
```
make clean
```
beforehand to remove the pyc file from previous compilation.

### Use
Below is a brief example of the basic usage of _hashmap_:
```
from hashmap import Hashmap

my_hash_table = Hashmap(15)

# set
my_hash_table.set("foo", "bar")
my_hash_table.set("foo2", 2")

# get
bar = my_hash_table.get("foo")      # "bar"

# overwrite
my_hash_table.set("foo", "hoe")

# delete
hoe = my_hash_table.delete("foo")   # "hoe"

# load
load_factor = my_hash_table.load()  # 0.0625
```

### Test
To test, use
```
make check
```
, or simply type ```make``` to run the test script.

## Limitation
Depending on the system, the collision of keys may vary. For example, on 64-bit system, when _size_ is 3, "foo" and "foo3" collides. As a potential improvement, the prehashing step described in the "__idx__" function of [hashmap.py](https://github.com/Ornithologist/hashmap_with_chaining/blob/master/hashmap.py) may change to other hashing mechanism.

This implementation is done with fixed-size hashmap in mind. In the situation where fixed-size is no longer a hard requirement, we can further improve the search performance of this _Hashmap_ by using open addressing. However, user needs to specify a _load_factor_ argument to prevent clustering.

For example:
```
my_hash_table = Hashmap(30, 0.75)
```
, or a default _load_factor_ would be given.

## References

* [__hash__()](https://docs.python.org/2.7/reference/datamodel.html#object.__hash__)

* [MIS Opencourseware](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec08.pdf)
* [java.util.Hashmap](http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/util/HashMap.java#HashMap.indexFor%28int%2Cint%29)
