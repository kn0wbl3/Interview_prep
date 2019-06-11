class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    def walk_ll(ll, result_LL):
        cur_node = ll.head
        while cur_node:
            try:
                x = cur_node.value / 1
                result_LL.append(cur_node.value)
                cur_node = cur_node.next
            except:
                raise ValueError('ERROR: Non int elements added to the Linked List. Closing Program')
        return result_LL

    union_ll = LinkedList()
    union_ll = walk_ll(llist_1, union_ll)
    union_ll = walk_ll(llist_2, union_ll)
    
    if union_ll.head is None:
        return None
    else:
        return union_ll

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_ll = LinkedList()
    set1 = set()
    
    cur_node = llist_1.head
    while cur_node:
        set1.add(cur_node.value)
        cur_node = cur_node.next
    
    cur_node = llist_2.head
    while cur_node:
        if cur_node.value in set1:
            intersection_ll.append(cur_node.value)
        cur_node = cur_node.next
    
    if intersection_ll.head is None:
        return None
    else:
        return intersection_ll


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

#edge case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

#edge case 2
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = ['a','b','n']
element_2 = ['z','r']

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
