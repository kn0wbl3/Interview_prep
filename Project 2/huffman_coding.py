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

def huffman_encoding(data):
    string_freq = determine_frequency(data)
    huff_root_node = create_huffman_tree(string_freq)
    encoded_dict = walk_tree(huff_root_node, prefix="", code={}) #returns dictionary of chars with encoded values
    encoded_msg = ''.join(encoded_dict.values()) #changes dict to single encoded message in the form of a string
    return encoded_msg
    
def huffman_decoding(data,tree):
    decoded_msg = []
    cur_node = tree[1]
    
    for char in data:
        if char == '0' and cur_node.left:
            cur_node = cur_node.left[1]
        elif cur_node.right:
            cur_node = cur_node.right[1]
            
        if not isinstance(cur_node, Tree_Node):
            decoded_msg.append(cur_node)
            cur_node = tree[1]
            
    return decoded_msg
    
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
        
        freq_q.put((left[0] + right[0], node)) #add new node onto priority queue
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
    
    


    
def tests():
    
    #determine_frequency tests
    x = determine_frequency('testing')
    assert sorted(x) == [('e', 1), ('g', 1), ('i', 1), ('n', 1), ('s', 1), ('t', 2)], 'determine_frequency tests # 1'
    
    x = determine_frequency('')
    assert x == None, 'determine_frequency tests # 2'
    
    #create_huffman_tree tests
    x = [('e', 1), ('g', 1), ('i', 1), ('n', 1), ('s', 1), ('t', 2)]
    huff_root_node = create_huffman_tree(x)
    assert(huff_root_node[0] == 7)
    
    
    #huffman encoding tests
    encoded_string = huffman_encoding("testing")
    assert(encoded_string == '0001001110110111')
    
    #huffman decoding tests
    decoded_string = huffman_decoding(encoded_string, huff_root_node)
    assert(''.join(decoded_string) == 'segtin')
    
    print('tests done')
    
tests()

'''
if __name__ == "__main__":
    codes = {}
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    #decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
'''