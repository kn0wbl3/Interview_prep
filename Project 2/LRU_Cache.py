from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.x = {}
        self.capacity = capacity
        self.tracker = deque() #use deque to keep track of what items were added in what order

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        return self.x.get(key, -1)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.get(key) < 0: 
            if len(self.x) == self.capacity:
                rem_elem = self.tracker.popleft()
                self.x.pop(rem_elem)
            self.x[key] = value
            self.tracker.append(key)
            
#test 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
assert(our_cache.get(1)==1)      # returns 1
assert(our_cache.get(2)==2)     # returns 2
assert(our_cache.get(3)==-1)     # return -1

our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6) #overflow on capacity, rem oldest item
assert(our_cache.x == {2:2, 3:3, 4:4, 5:5, 6:6})
assert(our_cache.tracker == deque([2, 3, 4, 5, 6]))


#test2 - only 1 cache space (edge case)
our_cache = LRU_Cache(1)
our_cache.set(1, 1)
our_cache.set(2, 2)
assert(our_cache.get(1)==-1)
assert(our_cache.get(2)==2)
assert(our_cache.get(3)==-1)

our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)
assert(our_cache.x == {6:6})
assert(our_cache.tracker == deque([6]))

#test3 --> duplicates
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(1, 1)
assert(our_cache.get(1)==1)
assert(our_cache.get(2)==-1)
assert(our_cache.get(3)==-1)

our_cache.set(1, 1)
our_cache.set(1, 1)
our_cache.set(1, 1)
our_cache.set(1, 1)
assert(our_cache.x == {1:1})
assert(our_cache.tracker == deque([1]))
