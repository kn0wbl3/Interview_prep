"""
With both stack and queues, we saw that trying to use arrays introduced some concerns regarding the time complexity, particularly when the initial array size isn't large enough and we need to expand the array in order to add more items.

With our stack implementation, we saw that linked lists provided a way around this issue—and exactly the same thing is true with queues.

Time Complexity:
So what's the time complexity of adding or removing things from our queue here?

Well, when we use enqueue, we simply create a new node and add it to the tail of the list. And when we dequeue an item, we simply get the value from the head of the list and then shift the head variable so that it refers to the next node over.

Both of these operations happen in constant time—that is, they have a time-complexity of O(1).
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.num_elements == 0:
            self.head = new_node
            self.tail = self.head
        else:    
            self.tail.next = new_node  # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            value = self.head.data
            self.head = self.head.next
            self.num_elements -= 1
            return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.size() == 0
        



def tests():
    q = Queue()
    #enqueue tests
    q.enqueue(1)
    assert(q.head.data == 1)
    assert(q.tail.data == 1)
    
    q.enqueue(2)
    q.enqueue(3)
    assert(q.head.data == 1)
    assert(q.tail.data == 3)
    
    #size tests
    assert(q.size() == 3)
    
    #is_empty tests
    assert(q.is_empty() == False)
    
    #dequeue tests
    # Setup
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    # Test size
    print ("Pass" if (q.size() == 3) else "Fail")
    
    # Test dequeue
    print ("Pass" if (q.dequeue() == 1) else "Fail")
    
    # Test enqueue
    q.enqueue(4)
    print ("Pass" if (q.dequeue() == 2) else "Fail")
    print ("Pass" if (q.dequeue() == 3) else "Fail")
    print ("Pass" if (q.dequeue() == 4) else "Fail")
    q.enqueue(5)
    print ("Pass" if (q.size() == 1) else "Fail")
        
    print('tests finished')

tests()