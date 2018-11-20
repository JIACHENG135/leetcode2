# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:37:40 2018

@author: ljc
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if matrix == [[]]:
            return False
        
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
        def divide_two_with_index(A,target,l,r):
            if target==A[r] or target == A[l]:
        #        print('run')
                return True
            elif target>A[r]:
                return r
            elif target<A[l]:
                return False
            else:
                if r-l <=1:
                    if target>=A[r]:
                        return r
                    elif target<A[l] and l>1:
                        return l-1
                    elif target == A[l]:
                        return l

                    elif target<A[l]:
                        return False
                    else:
                        return l
                else:
                    mid = (r+1+l)//2
                    if target==A[mid]:
                        return True
                    elif target>A[mid]:
                        l = mid
                        return divide_two_with_index(A,target,l,r)
                    else:
                        r = mid
                        return divide_two_with_index(A,target,l,r)
                    
        matrix_col_0 =[x[0] for x in matrix]

        a = divide_two_with_index(matrix_col_0,target,0,len(matrix_col_0)-1)
        #print(a,matrix[a],target,divide_two(matrix[a],target))
        if type(a) == bool and a==True:
            return True
        elif type(a) == bool and a==False:
            return False
        else:
            return divide_two(matrix[a],target)
