import sys
import queue

class Tree_Node(object):  
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def get_value(self):
        return self.value
    
    def set_value(self, new_val):
        self.value = new_val
        
    def get_left(self):
        return self.left
    
    def set_left(self, new_left):
        self.left = new_left
        
    def get_right(self):
        return self.right
    
    def set_right(self, new_right):
        self.right = new_right
        
    def has_left_child(self):
        return not (self.get_left() == None)
    
    def has_right_child(self):
        return not (self.get_right() == None)
    
    def __eq__(self,other):
        return 0
    
    def __lt__(self,other):
        return 0
    
    def __gt__(self,other):
        return 0
    
    def __getitem__(self, key):
        return self.value[key]

def huffman_encoding(data):
    string_freq = determine_frequency(data)
    encoded_data, tree_root = create_huffman_tree(string_freq)
    result = walk_tree(tree_root, prefix="", code={})
    print(result)
    
def huffman_decoding(data,tree):
    pass

def determine_frequency(string):
    if len(string) == 0:
        return None
    freq_dict = {}
    for char in string:
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1
    return freq_dict.items()

def create_huffman_tree(frequency_dict):
    freq_q = queue.PriorityQueue()
    for k, v in frequency_dict:
        freq_q.put((v, k))
    while freq_q.qsize() > 1:
        left, right = freq_q.get(), freq_q.get()
        node = Tree_Node()
        node.set_left(left)
        node.set_right(right)
        
        freq_q.put((left[0] + right[0], node))
    return freq_q.get()

def walk_tree(node, prefix="", code={}):
    if isinstance(node[1].left[1], Tree_Node):
        walk_tree(node[1].left,prefix+"0", code)
    else:
        code[node[1].left[1]]=prefix+"0"
    if isinstance(node[1].right[1],Tree_Node):
        walk_tree(node[1].right,prefix+"1", code)
    else:
        code[node[1].right[1]]=prefix+"1"
    return(code)
    
    
'''
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
''' 
    
def tests():
    
    #determine_frequency tests
    x = determine_frequency('testing')
    assert sorted(x) == [('e', 1), ('g', 1), ('i', 1), ('n', 1), ('s', 1), ('t', 2)], 'determine_frequency tests # 1'
    
    x = determine_frequency('')
    assert x == None, 'determine_frequency tests # 2'
    
    #create_huffman_tree tests
    x = [('e', 1), ('g', 1), ('i', 1), ('n', 1), ('s', 1), ('t', 2)]
    root, tree = create_huffman_tree(x)
    assert(root == 7)
    
    
    #huffman encoding tests
    result = huffman_encoding("testing")
    print(result)
    
    
        
    print('tests done')
    
tests()