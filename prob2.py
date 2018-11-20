# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:46:46 2018

@author: ljc
"""

def minD(A):
    set_al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 0
    row = len(A)
    col = len(A[0])
    for j in range(col):
#        print(j)
        for i in range(row-1):
            if A[i+1][j] not in set_al[set_al.index(A[i][j]):]:
#                print(set_al[set_al.index(A[i][j])+1:])
                count += 1
                break
            
    return count

a = minD(["rrjk","furt","guzm"])
print(a)