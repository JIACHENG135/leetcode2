# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:35:57 2018

@author: ljc
"""
import time
def spiral(A):
    A_keys = ['y','x','z','s'];
    A_bound = [len(A[0]),len(A),0,0]
    dictA = dict(zip(A_keys,A_bound))
    counter = 0
    key_counter = 0
    numb = len(A[0])*len(A)
    ans =[]
    i = 0
    j = 0
    while counter<numb:
#        print(dictA)
        if key_counter%4 == 0:
            while j<dictA[A_keys[key_counter%4]]:
#                print(i,j,A,A_keys[key_counter%4])
#                print('I run 0')
                ans.append(A[i][j])
                j += 1
                counter += 1
            print(j,counter)
            key_counter += 1
            i +=1
            j = j-1
            dictA['y'] -= 1
        elif key_counter%4 == 1:
            while i<dictA[A_keys[key_counter%4]]:
#                print(i,j,A,A_keys[key_counter%4])

                ans.append(A[i][j])
                i += 1
                counter += 1
            key_counter += 1
            i -= 1
            j -= 1
            dictA['x'] -= 1

        elif key_counter%4 == 2:
            while j>=dictA[A_keys[key_counter%4]]:
#                print(i,j,A,A_keys[key_counter%4],dictA[A_keys[key_counter%4]])
                ans.append(A[i][j])
                j -= 1
                counter += 1
            key_counter += 1
            j += 1
            i -= 1
            dictA['z'] += 1
        
        elif key_counter%4 == 3:
            while i>dictA[A_keys[key_counter%4]]:


                ans.append(A[i][j])
                i -= 1
                counter += 1
            key_counter += 1
            i += 1
            j += 1
            dictA['s'] += 1 
#        print(i,j,key_counter%4,A_keys[key_counter%4],dictA[A_keys[key_counter%4]],counter)
        time.sleep(1)

    return ans

a = spiral([[1,2,3,4],[4,4,5,6],[7,7,8,9]])
print(a)
            