# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 23:55:23 2018

@author: ljc
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:35:57 2018

@author: ljc
"""
import time
def spiralOrder(matrix):
    if not matrix:
        return []
    A_keys = ['y','x','z','s'];
    A_bound = [len(matrix[0]),len(matrix),0,0]
    dictA = dict(zip(A_keys,A_bound))
    counter = 0
    key_counter = 0
    numb = len(matrix[0])*len(matrix)
    ans =[]
    i = 0
    j = 0
    while counter<numb:
        print(dictA)
        if key_counter%4 == 0:
#            while j<dictA[A_keys[key_counter%4]]:
##                print(i,j,A,A_keys[key_counter%4])
##                print('I run 0')
#                ans.append(matrix[i][j])
#                j += 1
#                counter += 1
            ans = ans + matrix[i][j:dictA[A_keys[key_counter%4]]]
            counter = counter + len(matrix[i][j:dictA[A_keys[key_counter%4]]])
            j = j + len(matrix[i][j:dictA[A_keys[key_counter%4]]])

            key_counter += 1
            i +=1
            j = j-1
            dictA['y'] -= 1
        elif key_counter%4 == 1:
            while i<dictA[A_keys[key_counter%4]]:
                print('I run')

#                print(i,j,A,A_keys[key_counter%4])

                ans.append(matrix[i][j])
                i += 1
                counter += 1
#            ans = ans + 
#            print(dictA[A_keys[key_counter%4]])
#            print(matrix[i:dictA[A_keys[key_counter%4]]][j-1])
#            counter = counter + len(matrix[i:dictA[A_keys[key_counter%4]]][j-1])
#            i = i + len(matrix[i:dictA[A_keys[key_counter%4]]][j-1])
#            print(i,counter)
            key_counter += 1
            i -= 1
            j -= 1
            dictA['x'] -= 1

        elif key_counter%4 == 2:
            while j>=dictA[A_keys[key_counter%4]]:
#                print(i,j,A,A_keys[key_counter%4],dictA[A_keys[key_counter%4]])
                ans.append(matrix[i][j])
                j -= 1
                counter += 1
            key_counter += 1
            j += 1
            i -= 1
            dictA['z'] += 1

        elif key_counter%4 == 3:
            while i>dictA[A_keys[key_counter%4]]:


                ans.append(matrix[i][j])
                i -= 1
                counter += 1
            key_counter += 1
            i += 1
            j += 1
            dictA['s'] += 1 
#        print(i,j,key_counter%4,A_keys[key_counter%4],dictA[A_keys[key_counter%4]],counter)
        print(ans)
        time.sleep(1)

    return ans

a = spiralOrder([[1,2,3,4],[4,4,5,6],[7,7,8,9]])
#print(a)
            