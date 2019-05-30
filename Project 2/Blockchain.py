import hashlib

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.timestamp, self.data, self.previous_hash)
        
    def get_time(self):
        return self.timestamp
    
    def set_time(self, new_time):
        self.timestamp = str(new_time)
        
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = str(new_data)
        
    def get_prev_hash(self):
        return self.previous_hash
    
    def set_prev_hash(self, new_prev):
        self.previous_hash = str(new_prev)
        
    def get_hash(self):
        return self.hash
    
    def set_hash(self):
        self.hash = self.calc_hash(self.timestamp, self.data, self.previous_hash)

    def calc_hash(self, timestamp, data, prev_hash):
        sha = hashlib.sha256()
        concat = timestamp + ' ' + data + ' ' + prev_hash
        hash_str = concat.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
      
class Blockchain(object):
    def __init__(self):
        self.head = None
        
    def append(self, new_block):
        if self.head is None:
            self.head = new_block
        else:
            cur_block = self.head
            while cur_block != 'None':
                cur_block = cur_block.previous_hash
            cur_block.previous_hash = new_block
        
        
def tests():
    blk = Block('13:12 4/2/2019', 'test', None)
    assert(blk.get_hash() == 'e6b429b55b8858431a8aa282118006c80eb5e0570a8eb56c6d77c6ca0158cb25')
    
    blkA = Block('17:12 6/8/9', 'transaction complete', None)
    blkB = Block('17:12 15/12/28', 'transaction started', None)
    
    chain = Blockchain()
    chain.append(blk)
    chain.append(blkA)
    chain.append(blkB)
    
    print(chain)
    
    print('tests done')
tests()

'''
https://medium.com/coinmonks/building-a-simple-blockchain-data-structure-with-python-e7ebd448647a
import hashlib, json
block_genesis_serialized = json.dumps(block_genesis, sort_keys=True).encode(‘utf-8’)
'''