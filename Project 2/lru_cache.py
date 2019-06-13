from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.x = OrderedDict() #use OrderedDict to keep track of what items were added in what order
        self.capacity = capacity

    def get_val(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.x.get(key, -1) > 0:
            val = self.x[key]
            self.x.pop(key)
            self.x[key] = val
            return val
        else:
            return -1
        

    def set_val(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.get_val(key) < 0: 
            if len(self.x) == self.capacity:
                self.x.popitem(False) #remove the least recently used item (in the front of the dict)
            self.x[key] = value #add new item to the back of dict
            
#test 1
our_cache = LRU_Cache(5)

our_cache.set_val(1, 1)
our_cache.set_val(2, 2)
assert(our_cache.get_val(1)==1)      # returns 1
assert(our_cache.get_val(2)==2)     # returns 2
assert(our_cache.get_val(3)==-1)     # return -1

our_cache.set_val(3, 3)
our_cache.set_val(4, 4)
our_cache.set_val(5, 5)
our_cache.set_val(6, 6) #overflow on capacity, rem oldest item
assert(our_cache.x == {2:2, 3:3, 4:4, 5:5, 6:6})

assert(our_cache.get_val(2)==2)     # returns 2
assert(our_cache.x == {3:3, 4:4, 5:5, 6:6, 2:2}) #testing for keys being called again and sent to the back of the list


#test2 - only 1 cache space (edge case)
our_cache = LRU_Cache(1)
our_cache.set_val(1, 1)
our_cache.set_val(2, 2)
assert(our_cache.get_val(1)==-1)
assert(our_cache.get_val(2)==2)
assert(our_cache.get_val(3)==-1)

our_cache.set_val(3, 3)
our_cache.set_val(4, 4)
our_cache.set_val(5, 5)
our_cache.set_val(6, 6)
assert(our_cache.x == {6:6})

#test3 --> duplicates
our_cache = LRU_Cache(5)
our_cache.set_val(1, 1)
our_cache.set_val(1, 1)
assert(our_cache.get_val(1)==1)
assert(our_cache.get_val(2)==-1)
assert(our_cache.get_val(3)==-1)

our_cache.set_val(1, 1)
our_cache.set_val(1, 1)
our_cache.set_val(1, 1)
our_cache.set_val(1, 1)
assert(our_cache.x == {1:1})
