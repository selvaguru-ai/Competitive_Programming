#Two_Sum.py
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

input_list = [int(i) for i in input().split()]
dict = {}
def two_sum(input_list, target):
    for i,n in enumerate(input_list):
        m = target-n
        if m in dict:
            return [dict[m], i]
        else:
            dict[n] = i

print (two_sum(input_list, int(input())))