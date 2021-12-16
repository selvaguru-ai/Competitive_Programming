#Remove duplicates on the sorted list
#using two pointers in the same direction concept

def remove_duplicates(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast]!=arr[slow]:
            slow = slow+1
            arr[slow] = arr[fast]
    return slow+1

arr = [0,0,1,1,1,2,2,3,4,4,5]
value = remove_duplicates(arr)
print (arr[:value])
