import Chain
import random

blocks = [Chain.GenesisBlock(name = 'Main', password = 'MAIN', block_id = str(10))]

previous_digest = blocks[0].compute_hash()

for i in range(0, 10):
    random_id =  10
    block = Chain.Block(
        name = 'Prasanna', 
        password = 'Prasanna123', 
        previous_hash = previous_digest, 
        bolck_id = str(random_id)
    )
    blocks.append(block)
    previous_digest = block.compute_hash()


hashes = [i.getPreviousHash() for i in blocks[1:]]
print(hashes)


#check integrity of any block:
block_number = 5

#get hash of the block 5 and that hash is stored in 5+1th block , for any n block, n+1 block has its hash

#hash of that block
previous_digest = blocks[block_number +1].getPreviousHash()

#block:
block = blocks[block_number]

#check integrity:
Chain.check_integrity(block, previous_digest)


Chain.check_integrity_of_all_blocks(blocks)