# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:34:49 2018

@author: ljc
"""

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    a = [len(matrix[0])-1-i for i in range(len(matrix[0]))]*len((matrix[0]))
    b = [j//len((matrix[0])) for j in range(len(matrix[0])*len(matrix[0]))]
    matrix_new = [([0] *len(matrix[0])) for i in range(len(matrix[0]))]
    counter = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
#            print(a,b)
#            print(i,j,a[counter],b[counter],matrix[a[counter]][b[counter]])
            matrix_new[i][j] = matrix[a[counter]][b[counter]]
            counter += 1
    matrix = matrix_new
    return matrix


a = rotate([[1,2,3],[2,3,4],[3,4,5]])
print('a=',a)