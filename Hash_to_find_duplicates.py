hashNum = {}
nums = [int(i) for i in input().split()]
for i in nums:
    if i not in hashNum:
        #stores in a key/value pair with index starting from 0
        hashNum[i] = 0
    else:
        print ("True")
print ("False")