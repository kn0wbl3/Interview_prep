from collections import deque
'''
Trees: Very similar to linked lists, a "root" node and children nodes under it
Ways to search through trees:
    BFS: Breadth First Search - search each node of a level of a tree before moving to the next level
    -best for finding the shortest path
    
    DFS: Depth First Search - search from the root all the way to a leaf node, then start over
    -best for 
        -Pre-Order: Root, Left, Right
        -In-Order: Left, Root, Right
        -Post-Order: Left, Right, Root
        
Binary Search Trees:
    a specific type of binary tree
    every node to the left of a parent is smaller 
    every node to the right of the parent is larger
    
Runtime Stats for Binary Search Trees:
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

class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"
    
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root
    
    def set_root(self, new_val):
        self.root = Node(new_val)
        
        
    '''
    pre_order, in_order, and post_order are forms of the Depth First Search (DFS)
    '''    
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
    
    def bfs(tree):
        q = Queue()
        visit_order = list()
        node = tree.get_root()
        q.enq(node)
        while(len(q) > 0):
            node = q.deq()
            visit_order.append(node)
            if node.has_left_child():
                q.enq(node.get_left_child())
            if node.has_right_child():
                q.enq(node.get_right_child())
    
        return visit_order
    
    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1 # traverse left
        else: #new_node > node
            return 1  # traverse right
    
    def insert(self,new_value): #used for BSTs
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node's value
                node.set_value(new_node.get_value())
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping
                    
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s
    
    def search(self,value): #used for BSTs
        node = self.get_root()
        s_node = Node(value)
        while(True):
            comparison = self.compare(node,s_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False
