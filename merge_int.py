# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 08:48:07 2018

@author: ljc
"""
def twodivide(nums,target):
    def mid_divide(nums,l,r,target):
        
#        print(l,r)
        if target<nums[l]:
            return l
        elif target>nums[r]:
            return r
        elif r-l <= 2:

            return l
        else:
            mid = (l + r )// 2
            if target>nums[mid]:
                l = mid
                return mid_divide(nums,l,r,target)
            elif target<nums[mid]:
                r = mid
                return mid_divide(nums,l,r,target)
            else:
                return mid
        


    return mid_divide(nums,0,len(nums)-1,target)
def insert_sort(start_point,end_point,start_new,end_new):
    next_start_index = 
        
#        if end_point[s]>end_new:
#            pass
#        elif end_new>=start_point[s+1]:
#            if start_new < end_point[s]:
#
#                while end_new>=start_point[s+1]:
#                    s+=1
#                    print(s)
#                    if s>-1:
#                        end_point[-1] = end_new
#                        break
#    #            end_point[s] = end_point[s+1]
#                    start_point.pop(s)
#                    end_point.pop(s)
#                            
#            else:
#                while end_new>=start_point[s+1]:
#                    start_point[s] = start_new
#                    end_point[s] = end
#                    while end_new >end_point[s+1]:
        
                        
                    
                
                
        else:
            end_point[s] = end_new
    return [start_point,end_point]

def min_max(nums,start_new,end_new):
    s = -1
    while min(min(start_new,nums[s][0]),min(start_new,nums[s][-1])
    
    
    
def 
a = insert_sort([1,6,9],[2,7,12],4,)
print(a)

#def mergeint(nums):
#    start_point =[]
#    end_point = []
#    for i in range(len(nums)):
#        if nums[i][0]