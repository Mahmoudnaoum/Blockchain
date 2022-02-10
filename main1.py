from blockchain import Blockchain,Block
import time
import random


chain = Blockchain(2)
time_lst = []

randomNames= ["marwan", "ghandour", "naoumetous", "hammad", "simbo-limbo", "khairy", "beshara"
, "smith-rowe", "Diogo armando jottta"]

# Blocks Generation
for n in range(8):
    temp = Block("")
    k = random.randint(1,4)
    for z in range (k):
        while (1):
            i,j = random.randint(0,7),random.randint(0,7)
            Amount = random.randint(1,7)*8
            if i != j :
                temp.add_transaction(randomNames[i]+" pays " + randomNames[j]+ " "+ str(Amount) + "$")
                break

    # Mining
    start = time.time()
    chain.mine(temp)
    end = time.time()
    time_lst.append(end-start)

# Printing the Chain
chain.print_chain()
print(time_lst)
print("******************************************************")
print ('Average taken time:', sum(time_lst) / float(len(time_lst)))
print("Length of the chain:",chain.chain_len())
