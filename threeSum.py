# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:35:40 2018

@author: ljc
"""
import time
class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        list_n = [i for i in range(1,10)]
        results=[]
        result = []
        l = 0
        r = 8
        def threeSum(list_n,N,l,r,target,result,results):
#            print(target,result,list_n,list_n[r-N+1:])

            if target>sum(list_n[r-N+1:]) or target<list_n[0]:
                return
            else:
                if N==2:
                    while r>l:
#                        print(l,r)
#                        time.sleep(1)
                        if target<list_n[l]+list_n[r]:
                            r -=1
                            
                        elif target>list_n[l]+list_n[r]:
                            l+=1

                        else:
#                            print('==',l,r)
                            results.append(result+[list_n[l],list_n[r]])
#                            r-=1
                            l+=1

                else:
                    for i in range(1,len(list_n)):
#                        print(i)
                        threeSum(list_n[i:],N-1,0,len(list_n[i:])-1,target-list_n[i-1],result + [list_n[i-1]],results)
                        
                        
            return results
        
        return threeSum(list_n,k,l,r,n,result,results)
    
    
a = Solution()
b = a.combinationSum3(4,24)
print(b)