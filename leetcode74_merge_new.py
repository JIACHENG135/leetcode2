# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:41:05 2018

@author: ljc
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def divide_two(A,target):
            if target>A[-1] or target<A[0]:
                return False
            else:
                if len(A) <=2:
                    if target not in A:
                        return False
                    else:
                        return True
                else:
                    mid = len(A)//2
                    if target==A[mid]:
                        return True
                    elif target>A[mid]:
                        return divide_two(A[mid:],target)
                    else:
                        return divide_two(A[0:mid],target)
                    
        if not matrix:
            return False
        if matrix == [[]]:
            return False
        mall = []
        for i in matrix:
            mall = mall + i
            
        return divide_two(mall,target)
    
    
a = Solution()
b = a.searchMatrix([[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]],30)
print(b)
        
