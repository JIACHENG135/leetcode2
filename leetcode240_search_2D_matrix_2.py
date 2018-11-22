# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:32:42 2018

@author: ljc
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
#        l2 = [1,3,8,10]
#        l1 = [2,4,6]
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
        def merge_sort(l1,l2):
            if l1:
                k = -2
                
                while l1:
                    _ = l1.pop()
                    while abs(k)<=len(l2) and _ < l2[k]:
                        k -= 1
                    l2.insert(k+1,_)
                    k -= 1
                return l2
            else:
                return l2
            
            
        def inmatrix(matrix):
            #print(target)
            for i in range(min_n)[::-1]:
                #print(i,matrix[i][0],matrix[0][i])
                _min = min(matrix[i][0],matrix[0][i])
                if target >= _min:
                    l2 = merge_sort(matrix[i][0:i],matrix[0:i+1][i])
                    print('l2',l2,matrix[i][0:i],matrix[0:i+1][i])
                    if divide_two(l2,target):
                        return True
            return False
        min_n = min(len(matrix),len(matrix[0]))
        print(matrix,min_n)
        if min_n !=len(matrix):
            if inmatrix(matrix):
                return True
            elif matrix[min_n][0]==target:
                return True
            else:
                return self.searchMatrix(matrix[min_n:], target)
        else:
            return inmatrix(matrix)
            
a = Solution()
matrix = [[4,7,11,12,16,21,23,26],
          [5,12,17,17,18,23,26,31],
          [8,15,21,25,26,29,33,34],
          [13,20,26,26,29,34,39,40],
          [18,21,31,36,41,42,42,44],
          [19,23,31,39,46,49,50,53],
          [23,25,33,40,50,51,55,60],
          [27,28,33,44,51,56,61,65],
          [32,35,39,66,54,56,65,68],
          [33,38,40,49,56,57,66,71]]

target = 66
b= a.searchMatrix(matrix,target)
print(b)