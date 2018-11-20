# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:09:23 2018

@author: ljc
"""

class Solution(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def twoSum(self,A,B):
        result_1 = A + B
        result_2 = self.threeSum(A,B)
        return result_1,result_2
    def threeSum(self,A,B):
            return A+B
        
        
c = Solution('Bob','80')
print(c)
[d1,d2] = c.twoSum(20,40)
print(d1,d2)

        