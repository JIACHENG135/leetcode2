# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:23:40 2018

@author: ljc
"""
import time
def partition(A,p,r):
    counter = p-1
    x = A[r]
    for i in range(p,r):
        if A[i]<=x:
            counter += 1
            A[i],A[counter] = A[counter],A[i]
    q = counter +1
    A[q],A[r] = A[r],A[q]

    return q
    
def quick_sort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)

        
    


A = [3,6,9,1,2.5,1.5,0.5]
quick_sort(A,0,len(A)-1)

print(A)