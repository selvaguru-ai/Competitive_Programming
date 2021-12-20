#Code to add all zeros to the end of the array/list
#https://algo.monster/problems/move_zeros
def move_zeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast]!=0:

            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow+= 1
    return nums

nums = [int(x) for x in input().split()]

print(move_zeros(nums))


