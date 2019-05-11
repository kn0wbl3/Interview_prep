class Stack(object):
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
        
    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1
        
    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(self.arr))]
        for i, data in enumerate(old_arr):
            self.arr[i] = data
            
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return (self.num_elements == 0)
    
    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        
        self.next_index -= 1
        self.num_elements -= 1
        
        ans = self.arr[self.next_index]
        self.arr[self.next_index] = 0 #remove the value from the stack
        
        return ans
    
def tests():
    test_stck = Stack()
    nums = [4, 24, -80, 5, 28, 11, 10, 1, 2, 3, 14, 6]
    
    #testing push
    for i in range(10):
        test_stck.push(nums[i])
    assert(test_stck.arr == [4, 24, -80, 5, 28, 11, 10, 1, 2, 3])
    
    #testing handle_stack capacity
    test_stck.push(100)
    assert(test_stck.arr == [4, 24, -80, 5, 28, 11, 10, 1, 2, 3, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    #testing size
    assert(test_stck.size() == 11)
    
    #testing pop
    rem_data = test_stck.pop()
    assert(rem_data == 100)
    test_val = 0
    j = -1
    while test_stck.arr[j] == 0:
        j -= 1
    test_val = test_stck.arr[j]
    assert(test_val == 3)
    
    print('tests finished')
    
tests()