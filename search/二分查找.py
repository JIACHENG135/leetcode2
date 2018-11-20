# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 23:42:53 2018

@author: ljc
"""
import numpy as np
def searchMatrix(matrix, target):
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
        print(l,r)
        if target>A[r] or target<A[l]:
            return False
        elif target==A[r] or target == A[l]:
            return True
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
    print(a,matrix[a],target,divide_two(matrix[a],target))
    if type(a) == bool:
        if a==True:
            return True
        else:
            return False
    else:
        return divide_two(matrix[a],target)

x = np.random.randint(1,10,size = [8])
y = np.random.randint(5,8,size = [1])
x.sort()
#print(x,y,divide_two_with_index([1,3,5,7],3,0,3))
#print(divide_two_with_index([1,10,23],3,0,2))
print(searchMatrix([[1]],1))