# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:11:03 2018

@author: ljc
"""
import numpy as np
def set_zero(A):
    def sent_counter_h(A,i,j,row_0,col_0,back=1):
        # back means to end
        while (-1)**back*j>(-1)**back*(len(A[0])-1)*back:
            j = j + (-1)**(1-back)
            if j>-1 and A[i][j]==0:
                col_0.append(j)
                sent_counter_v(A,i,j,row_0,col_0)
        return row_0,col_0
    def sent_counter_v(A,i,j,row_0,col_0):
        while i<len(A)-1:
            i+=1
            print(i)
            if A[i][j]==0:
                row_0.append(i)
#                [row_0,col_0] = 
                sent_counter_h(A,i,j,row_0,col_0,1)
#                [row_0,col_0] = 
                sent_counter_h(A,i,j,row_0,col_0,0)
                
        return row_0,col_0
    def ro_ra(A):
        col_0 = []
        row_0 = []
        a_row = len(A)
        a_col = len(A[0])
        i = 0
        while i in range(a_row):
    #        print(i)
            if i not in row_0:
                j = 0
                while j in range(a_col):
    #                print(i,j,a_col,row_0,col_0)
                    if j not in col_0:
    
                        if A[i][j] == 0:
    #                        print(i,j)
                            col_0.append(j)
                            row_0.append(i)
                            [row_0,col_0] = sent_counter_h(A,i,j,row_0,col_0,1)
                            [row_0,col_0] = sent_counter_v(A,i,j,row_0,col_0)
                    j += 1
                
            i += 1
            
        return list(set(row_0)),list(set(col_0))
    [a,b] = ro_ra(A)
    A = np.array(A)
    A[a,:] = 0
    A[:,b] = 0
    return A
A = [[1,1,1],[1,0,1],[1,1,1]]
a= set_zero(A)
print(a)