'''
Trees: Very similar to linked lists, a "root" node and children nodes under it

Ways to search through trees:
    BFS: Breadth First Search - search each node of a level of a tree before moving to the next level
    
    DFS: Depth First Search - search from the root all the way to a leaf node, then start over
        -Pre-Order: Root, Left, Right
        -In-Order: Left, Root, Right
        -Post-Order: Left, Right, Root
    
Binary Search Trees:
    a specific type of binary tree
    every node to the left of a parent is smaller 
    every node to the right of the parent is larger
    
Runtime Stats:
            Worst Case   Average Case
    Search       O(n)      log(n)
    
    Insert       O(n)      log(n)
    
    Delete       O(n)      log(n)
'''

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        
    def get_value(self):
        return self.value
    
    def set_value(self, new_val):
        self.value = new_val
        
    def get_left_child(self):
        return self.left
    
    def set_left_child(self, new_left):
        self.left = new_left
        
    def get_right_child(self):
        return self.right
    
    def set_right_child(self, new_right):
        self.right = new_right
        
    def has_left_child(self):
        return not (self.get_left_child() == None)
    
    def has_right_child(self):
        return not (self.get_right_child() == None)
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root
    
    def set_root(self, new_val):
        self.root = Node(new_val)
        
    def pre_order(tree):
        visit_order = list()
        root = tree.get_root()
        
        def traverse(node):
            if node:
                visit_order.append(node.get_value())
                traverse(node.get_left_child())
                traverse(node.get_right_child())
        
        traverse(root)
        return visit_order
        
    def in_order(tree):
        visit_order = list()
        root = tree.get_root()
    
        def traverse(node):
            if node:
                traverse(node.get_left_child())
                visit_order.append(node.get_value())
                traverse(node.get_right_child())
        
        traverse(root)
        return visit_order
    
    def post_order(tree):
        visit_order = list()
        root = tree.get_root()
    
        def traverse(node):
            if node:
                traverse(node.get_left_child())
                traverse(node.get_right_child())
                visit_order.append(node.get_value())
    
        traverse(root)
        return visit_order