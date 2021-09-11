
def hashing_func(key):
    return key % len(hash_list)

def insert_hash(hash_list,key,value):
    hash_key = hashing_func(key)
    hash_list[hash_key]= value
    return hash_list

master_list = [i for i in input().split()]
hash_list= [None]*len(master_list)

for i in range(0, len(hash_list)):
    key = i
    value = master_list[i]
    hash_list = insert_hash(hash_list,key, value)
print (hash_list)