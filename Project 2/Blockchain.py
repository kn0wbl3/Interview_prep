import hashlib
import json

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash([self.timestamp, self.data, self.previous_hash])
        
    #Not adding any set methods, in blockchain once something is written to the chain it never changes!   
    def get_time(self):
        return self.timestamp
        
    def get_data(self):
        return self.data
        
    def get_prev_hash(self):
        return self.previous_hash
        
    def get_hash(self):
        return self.hash

    def calc_hash(self, item):
        sha = hashlib.sha256()
        concat = json.dumps(item) #need json.dumps to turn the list into a string that can be encoded
        '''
        https://medium.com/coinmonks/building-a-simple-blockchain-data-structure-with-python-e7ebd448647a
        '''
        hash_str = concat.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
      
class Blockchain(object):
    def __init__(self):
        self.head = None
        
    def prepend(self, new_block):
        if self.head is None:
            self.head = new_block
        else:
            new_block.previous_hash = self.head.get_hash()
            self.head = new_block
        
def tests():
    blk = Block('13:12 4/2/2019', '1', 0)
    blkA = Block('17:12 6/8/9', '2', 0)
    blkB = Block('17:12 15/12/28', '3', 0)
    
    chain = Blockchain()
    chain.prepend(blk)
    chain.prepend(blkA)
    chain.prepend(blkB)
    
    assert(chain.head.previous_hash == blkA.hash)
    assert(blkA.previous_hash == blk.hash)
    
    #test case 2: block with prev_hash already set
    blk = Block('18:18 4/2/2019', '1', '7b176106329acb0fb7c966445403f4909abe2dafd5caa09f9676307aa80d8c87')
    blkA = Block('17:12 6/8/9', '2', 0)
    blkB = Block('17:12 15/12/28', '3', 0)
    
    assert(blk.get_prev_hash() == blkA.get_hash())
    
    #test case 3: no data in blocks
    blk = Block('', '', '')
    blkA = Block('', '', '')
    blkB = Block('', '', '')
    
    chain = Blockchain()
    chain.prepend(blk)
    chain.prepend(blkA)
    chain.prepend(blkB)
    
    assert(chain.head.previous_hash == blkA.hash)
    assert(blkA.previous_hash == blk.hash)
    
    print('tests done')
tests()
