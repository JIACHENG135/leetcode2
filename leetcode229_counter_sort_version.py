# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:11:42 2018

@author: ljc
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l = min(nums)
        if min(nums)<0:
            
            nums = [i + (0 - min(nums)) for i in nums]
        conspace = [0 for i in range(min(nums),max(nums)+1)]
        #print(conspace)

        for i in nums:
            conspace[i-min(nums)] += 1

        res = []
#        counter = 0
#        print(conspace[conspace.index(max(conspace))],len(nums)//3)
        while conspace and conspace[conspace.index(max(conspace))]>len(nums)//3:
                

                res.append(conspace.index(max(conspace))+l)
                conspace[conspace.index(max(conspace))]=0
                
        return res
    
    
    
a = Solution()
b = a.majorityElement([-7,-6,-6,2])
print(b)
