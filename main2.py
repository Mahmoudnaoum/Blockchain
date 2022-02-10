from blockchain import Blockchain,Block
import time , random , copy

def change_chain(bc,id):
    global chain
    global current_chain

    global_chain,local_chain =  chain.chain_len(),bc.chain_len()
    if global_chain <local_chain:
        chain= copy.deepcopy(bc)
        current_chain_id = id
        print("chain replaced by user:",id)
        print("chain lenght:",bc.chain_len(),"chain owner" ,current_chain_id )
    else :
        print("falied to replace the chain with user:",id)


randomNames= ["marwan", "ghandour", "naoumetous", "hammad", "simbo-limbo", "khairy",
"beshara", "smith-rowe", "Diogo armando jottta"]

chain = Blockchain(4)
current_chain_id =0
blocks = []

for n in range(7):
    temp = Block("")
    k = random.randint(1,4)
    for z in range (k):
        while (1):
            i,j = random.randint(0,7),random.randint(0,7)
            Amount = random.randint(1,7)*8
            if i != j :
                temp.add_transaction(randomNames[i]+" pays " + randomNames[j]+ " "+ str(Amount) + "$")
                break
    blocks.append(copy.deepcopy(temp))

miner_chain = copy.deepcopy(chain)
attacker_chain = copy.deepcopy(chain)
# number of blocks  
attacker_index = miner_index = 0
while (len(blocks)>miner_index and len(blocks)>attacker_index ):
    # Mining computing power
    miner_chance = attacker_chance = random.randint(1,100) 
    if miner_chance >0 and miner_chance <40 :

        miner_chain.mine(blocks[miner_index])
        change_chain(miner_chain,0)
        miner_index += 1

    if attacker_chance >41 and attacker_chance<101:
        attacker_chain.mine(Block("attack"+str (attacker_index)))
        change_chain(attacker_chain, 1)
        attacker_index += 1


print(9 * '-' + '\n' + 'CORRECT CHAIN ')
chain.print_chain()
print(9 * '-' + '\n' + 'MINER CHAIN ')
miner_chain.print_chain()
print(9 * '-' + '\n' + 'ATTACKER CHAIN ')
attacker_chain.print_chain()