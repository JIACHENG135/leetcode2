# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:44:00 2018

@author: ljc
"""

def canJump(nums):
    result = []
    results = []
    def jump(first,nums,result,results):
        if first == 0:
            for i in results:
                nums[i] = 0
        if first>=len(nums):
            result.append(0)

        else:
            rev = range(first)[::-1]
            iter_f = iter(rev)                
            while not result:
                try:
                    x = next(iter_f)
                    results.append(x)
                    jump(nums[x],nums[x+1:],result,results)
                except StopIteration:
                    break
            return result
    jump(nums[0],nums[1:],result,results)
    if not result:
        return False
    else:
        return True
        
                    

    jump(nums[0],nums[1:],result)
    if not result:
        return False
    else:
        return True
nums = [3,2,1,0,4]
a = canJump(nums);
print(a)