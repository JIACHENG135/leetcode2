# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:32:34 2018

@author: ljc
"""
def ro_matrix(matrix):
    if not matrix:
        return []
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        matrix[i] = matrix[i][::-1]
            
    return matrix
def rotate(matrix):

    matrix_n = len(matrix)
    
    if matrix_n <= 1: 
        return

    i, tmp_value = 0, matrix[0][0]
    start_x, start_y, coor_x, coor_y = 0, 0, 0, 0
    
    for i in range(matrix_n**2):
        
        trans_x, trans_y = transform(coor_x, coor_y, matrix_n)
        
        tmp_value, matrix[trans_x][trans_y] = matrix[trans_x][trans_y], tmp_value
        
        if (trans_x == start_x) and (trans_y == start_y):
            start_x, start_y = nextStart(start_x, start_y, matrix_n)
            coor_x, coor_y = start_x, start_y
            tmp_value = matrix[start_x][start_y]
        else:
            coor_x, coor_y = trans_x, trans_y
            
    return matrix
def transform(x, y, n):
    return y, abs(n-1-x)

def nextStart( x, y, n):
    
    y += 1
    if ((x+y) == (n-1)):
        x += 1
        y = x
        
    return x, y
                    
        
        
matrix=[[1,2,3],[2,3,4],[3,4,5]]
print(rotate(matrix))