# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:30:16 2018

@author: ljc
"""
import time
def permutation_01(n,k):
    first = [1 for i in range(k)] + [0 for i in range(len(n)-k)]
    last = [0 for i in range(len(n)-k)] + [1 for i in range(k)]
    permu = []
    
    while first != last:
        permu.append(list(filter(lambda x: x!=0,list(map(lambda i,j:i*j,first,n)))))
        counter = 0
        
        for i in range(len(n)-1):
            if first[i] == 1:
                counter += 1
                if first[i+1]==0:
                    first[i],first[i+1] = first[i+1],first[i]
                    first[0:i] = [1 for j in range(counter-1)] + [0 for j in range(i-counter+1)]
                    break
    permu.append(list(filter(lambda x: x!=0,list(map(lambda i,j:i*j,last,n)))))
    return permu

    
        

b = permutation_01([1,2,3,4,5],2)
print(b)