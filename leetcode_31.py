# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:40:09 2018

@author: ljc
"""
def re_sort(nums,index):
    temp = nums[0:index+1] 
    need_sort = nums[index[-1]+1:]
    need_sort.sort()
    nums = temp + need_sort
    return nums
def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
        

    """
    import copy
    target = 0
    nums_d = copy.copy(nums)
    nums_d.sort()
    nums_d_inv = nums_d[::-1]
    if nums == nums_d_inv:
        nums.sort
    else:
        for i in range(len(nums)-1,-1,-1):

            if nums[i] > nums[i-1]:
                target = i-1
                break
                
    nums_fore = nums[0:target+1]
    nums_hou = nums[target+1:]

    nums_hou.reverse()
    nums = nums_fore + nums_hou
    for i in range(target,len(nums)):

        if nums[i]>nums[target]:

            nums[target],nums[i] = nums[i],nums[target]
        
        
    print(nums)
    
    
a= nextPermutation([1,2,3])
print(a)