# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:07:24 2018

@author: ljc
"""

def isMt(A):
    counter_b = 0
    count = 0
    count_p = 0
    if len(A)<3:
        return False
    while count < len(A)-2:
        if A[count+2]<A[count+1] and A[count]<A[count+1]:
            counter_b += 1
#            print(counter_b)
        if A[count+1]==A[count]:
            return False
        elif A[count+2]>=A[count+1] and A[count]>=A[count+1]:
            count_p +=1
        count += 1    
    if counter_b == 1 and count_p == 0 :
        return True
    else:
        return False
    
print(isMt([0,3,2,1,-1]))