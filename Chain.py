import hashlib
import random

class Block():

    def __init__(self, name, password, previous_hash, bolck_id):
        self.name = name
        self.password = password
        self.previous_hash = previous_hash
        self.bolck_id = bolck_id
    

    def compute_hash(self):
        hash_ = hashlib.sha256(
            str(self.name+self.previous_hash+self.bolck_id+self.password).encode()
        )
        return str(hash_.hexdigest())
    
    def getPreviousHash(self):
        return self.previous_hash


def check_integrity(block, hash_):

    #compute hash for current 'block':
    current_hash = block.compute_hash()
    print(current_hash, hash_)
    if current_hash == hash_:
        print('Integrity verified')
    
    else: print('Integrity violated')

class GenesisBlock():

    def __init__(self, name, password, block_id):
        #create  genesis now only:
        self.name = name
        self.password = password
        self.bolck_id = block_id
    

    def compute_hash(self):
        hash_ = hashlib.sha256(
            str(self.name+self.password+self.bolck_id).encode()
        )

        return str(hash_.hexdigest())


def check_integrity_of_all_blocks(blocks):
    count = 0
    for i in range(0, len(blocks)):
        j = (i+1)%len(blocks)
        if j < i: print('no more blocks')
        else:
            hash_of_i = blocks[i].compute_hash()
            hash_of_j = blocks[j].getPreviousHash()
            if hash_of_i != hash_of_j:
                print('Integrity test failed')
                break
            count+=1
    else:
        print('Integrity test successful, no. of blocks counted : ', count)

            
