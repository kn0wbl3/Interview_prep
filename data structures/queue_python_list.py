"""
This Queue implementation uses a python list. 
Python list PROS:
    1) quickly provides meta data like size of the list
Python list CONS:
    1) O(n) add/delete times
    2) needs one contiguos block of memory
"""

class Queue():
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        # if queue is already full --> increase capacity
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()
        
        # enqueue new element
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr) #let's break this down below
        '''
        (self.next_index + 1) --> this is simple. taking the next_index counter and incrementing by 1
        % len(self.arr)       --> this is the tricky one. for numbers 1-10, if you modulo that number against
        10 then you will get that number back. We use this trick to wrap around the array to come back to index 0
        when we hit the limit of the array. You can try this with the below code to see:
            for i in range(10):
                print((i+1) % 10)
        '''
        if self.front_index == -1:
            self.front_index = 0
    
    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1   # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr) #this moves the front of the queue to the next index spot, thus removing the old "front"
        self.queue_size -= 1
        return value
            
    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0
    
    def front(self):
        # check if queue is empty
        if self.is_empty():
            return None
        return self.arr[self.front_index]
    
    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]

        index = 0

        # copy all elements from front of queue (front-index) until end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # case: when front-index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # reset pointers
        self.front_index = 0
        self.next_index = index

def tests():
    #__init__ tests
    q = Queue()
    assert(q.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    #enqueue tests
    q.enqueue(1)
    assert(q.arr == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(2, 12):
        q.enqueue(i)
    assert(q.arr == [11, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    #dequeue tests
    q.dequeue()
    assert(q.front_index == 1)
    q.dequeue()
    q.dequeue()
    assert(q.front_index == 3)
    
    print('tests finished')

tests()