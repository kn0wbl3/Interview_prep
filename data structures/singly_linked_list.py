# -*- coding: utf-8 -*-
"""
THIS PROJECT SHOWS HOW TO IMPLEMENT A SINGLY LINKED LIST AND ALSO HAS TEST CODE TO MAKE SURE IT IS RUNNING PROPERLY
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        
        # TODO: Write function to prepend here  
        if self.head is None:
            self.head = Node(value)
            return
        
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    
    def append(self, value):
        """ Append a value to the end of the list. """
        
        # TODO: Write function to append here
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
    
    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        
        # TODO: Write function to search here
        cur_node = self.head
        while cur_node:
            if cur_node.value == value:
                return cur_node.value
            cur_node = cur_node.next
        
        return False
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        
        # TODO: Write function to remove here
        cur_node = self.head
        prev_node = None
        found = False
        
        while cur_node and (found is False):
            if cur_node.value == value:
                found = True
            else:
                prev_node = cur_node    
                cur_node = cur_node.next
        
        if prev_node == None:
            self.head = self.head.next
            return True
        elif found == True:
            prev_node.next = cur_node.next
            return True
        else:
            return False
            
    
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        
        # TODO: Write function to pop here
        result = self.head.value
        self.head = self.head.next
        return result
        
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        
        # TODO: Write function to insert here
        new_node = Node(value)
        cur_node = self.head
        prev_node = None
        counter = 0
        while (counter < pos) and (cur_node.next):
            prev_node = cur_node
            cur_node = cur_node.next
            counter += 1
            
        if prev_node is None:
            new_node.next = self.head
            self.head = new_node
        elif (cur_node.next is None):
            cur_node.next = new_node
        else:
            new_node.next = cur_node
            prev_node.next = new_node
    
    def size(self):
        """ Return the size or length of the linked list. """
        # TODO: Write function to get size here
        size = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            size += 1
        return size
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
    
## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.prepend(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 3, 1], f"list contents: {linked_list.to_list()}"


# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1) == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4) == 4, f"list contents: {linked_list.to_list()}"
assert linked_list.search(8) == False, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"


print('tests finished.')
