# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 22:00:01 2018

@author: ljc
"""
import time
def canJumpp(nums):
    i=0
    zero_list = []
#    result = 1
    while True:
#        print(nums,i)
        if sum(nums[:-1]) != 0:

            if nums[i]<len(nums[i+1:]):

                if nums[i + nums[i]] == 0 and i + nums[i] not in zero_list: 
                    zero_list.append(i+nums[i])
                    zero_list.append(i)
                    temp_k = i
                    i = i + nums[i] - 1
                    nums[temp_k] = 0
                    
#                    print(i,'run',nums)
                    while nums[i] == 0:
#                        print(i)
                        i = i -1
                elif i+nums[i] in zero_list:
                    print(i,'run',nums)
                    zero_list.append(i)
                    nums[i] = 0
                    i -= 1
                    while nums[i]==0 and i>-1:
                        i -= 1
                else:
                    i = i + nums[i]
            else:
                return True
        else:
            return False
    time.sleep(1)

nums = [2,1,0,0]
a = canJumpp(nums);
print(a)