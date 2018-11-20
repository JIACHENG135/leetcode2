# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:19:50 2018

@author: ljc
"""

def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for n in nums:
        ind = abs(n) - 1
        if nums[ind] < 0:
            ans.append(abs(n))
        nums[ind] = - nums[ind]

    return ans
a = findDuplicates([1,1,2,10,10])
print(a)