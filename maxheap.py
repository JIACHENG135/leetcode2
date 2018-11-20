# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:16:41 2018

@author: ljc

"""

def max_heap(A,i):
    heapsize = len(A) - 1
    l = 2*(i+1)-1# the index in python of range(n) is from 0 1 ... to n-1 so consider i = 0, we should not
    r = 2*(i+1)+1-1# simply substrac 1 cause 2*i-1 = -1 rather than 1
    if l<=heapsize and A[i]<A[l]:
        largest = l
    else:
        largest = i      
    if r<=heapsize and A[largest]<A[r]:
        largest = r
    if largest!=i:
        A[i],A[largest] = A[largest],A[i]
        
#        time.sleep(2)
        return max_heap(A,largest)
    return A
        
def make_max_heap(A):
    """
    since index: len(A)//2  len(A)//2+1 ... len(A)//2 + n - 1 if the leaf for tree A
    easy to prove just because  2 * n//2 >= n -1
    """
    need_max = range(len(A)//2)[::-1]
    for i in need_max:
#        print(i)
        max_heap(A,i)

    return A

def heap_sort(A):
    """
    first make A as a max_heap
    than switch A[0] to the last element of the heap
    heap_size - 1 till heap_size == 0
    """
    make_max_heap(A)
    heap_size = len(A)
    while heap_size>0:
        A[0],A[heap_size-1] = A[heap_size-1],A[0]
        A = max_heap(A[0:heap_size-1],0) + A[heap_size-1:]
        heap_size-=1
    return A

def heap_extract_max(A):
    A = make_max_heap(A)
    if len(A)<1:
        print('it\'s not a heap ')
    max_A = A[0]
    A[0],A[-1] = A[-1],A[0]
    A = max_heap(A[:-1],0)
    return A,max_A

def heap_insert_key(A,i,key):
    if key<A[i]:
        print('key is too small')
        return A
    else:
        A[i] = key
#        pai = 
        while (i+1)//2-1 >=0 and A[(i+1)//2-1]<A[i]:
            A[(i+1)//2-1],A[i] = A[i],A[(i+1)//2-1]
            i = (i+1)//2-1
        return A
def max_heap_insert(A,key):
    A.append(float('-inf'))
    A = heap_insert_key(A,len(A)-1,key)
    return A
    
    
    
    
max_test = max_heap_insert([28, 6, 7, 5, 1, 3, 4],19)
print(max_test)
#max_test.max_heap([1,2,3],5)