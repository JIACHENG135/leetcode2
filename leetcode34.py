# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 22:07:20 2018

@author: ljc
"""
import time

class Solution:
    def searchRange( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        elif len(nums) == 1:
            return [0,0]
        
        def search_f(nums,nums_all,target,l,r):
            if (len(nums) == 1 and [target] != nums) or (len(nums) == 2 and target not in nums):
                return [-1,-1]
#            elif len(nums) == 2 and target in nums:
                
            if target>nums_all[-1] or target<nums_all[0]:
                return [-1,-1]
            mid = l + round(len(nums)/2)
            print(len(nums),mid)
            if target>nums_all[mid]:
                print('>',nums_all[mid:r+1],nums_all,len(nums_all[0:mid]),r)
                time.sleep(3)
                return search_f(nums_all[mid:r+1],nums_all,target,len(nums_all[0:mid]),r)
            elif target == nums_all[mid]:
                mid_1 = mid
                mid_2 = mid

                while nums_all[mid_1] == target:
                    mid_1 -= 1
                    if mid_1<0:
                        break
                while nums_all[mid_2] == target:
                    mid_2 += 1
                    if mid_2>len(nums_all)-1:
                        break
                return [mid_1+1,mid_2-1]

            else:
                print('<',l,mid,len(nums_all[l:mid]),nums_all[l:mid])
                return search_f(nums_all[l:mid],nums_all,target,l,l+len(nums_all[l:mid]))
        a = search_f(nums,nums,target,0,len(nums)-1)
        return a  
    
    
nums = [0,0,1,1,1,2,4,4,4,4,5,5,5,6,8,8,9,9,10,10,10]


a = Solution.searchRange(nums,8)
print(a)           