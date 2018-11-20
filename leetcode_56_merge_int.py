# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:25:18 2018

@author: ljc
"""

def twodivide(nums,target):
    def mid_divide(nums,l,r,target):
        
#        print(l,r)
        if target<nums[l]:
            return -1
        elif target>nums[r]:
            return -2
        elif target == nums[l]:
            return l
        elif target == nums[r]:
            return r
        elif r-l <= 1:
            
            if target>nums[l]:
                return l + 1
            
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
        
def merge(self,intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals) <= 1: return intervals
    ans = []
    intervals.sort(key=lambda interval: interval.start)
    
    start = intervals[0].start
    end = intervals[0].end
    
    for interval in intervals:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            ans.append(Interval(start, end))
            start = interval.start
            end = interval.end
            
    ans.append(Interval(start, end))
    return ans
        

    return mid_divide(nums,0,len(nums)-1,target)
        
def merge_int(nums):
    if len(nums) == 1:
        return nums
    else:
        start_point = []
        end_point = []
        for i in range(len(nums)-1):
            start_point.append(nums[i][0])
            end_point.append(nums[i][1])
            next_start = twodivide(start_point,nums[i+1][0])
#            print(start_point,i)
            if next_start== len(start_point)-1:
#                if nums[i+1][0] == start_point[-1]:
                next_end = twodivide(end_point,nums[i+1][1])
                if next_end == -2:
                    end_point[-1] = nums[i+1][1] 
#                    else:
#                        pass# because nums[i+1][0]>num[s][1] when next_start
            elif next_start == 0:
                while end_point[0]<nums[i+1][1]:
                    end_point.pop(0)
                    start_point.pop(0)
                end_point = [nums[i+1][1]] + end_point
                start_point = [nums[i+1][0]] + start_point   
            elif next_start == -2:
                next_start_start = twodivide(end_point,nums[i+1][0])
                print(next_start_start)
                if next_start_start == -2:
                    start_point.append(nums[i+1][0])
                    end_point.append(nums[i+1][1])
                elif next_start_start == len(end_point)-1:
#                    start_point.pop()
                    end_point[-1] = nums[i+1][1]
                else:
                    end_point[next_start_start] = nums[i+1][1]
#                if nums[i+1][1]>end_point[-1]:
#                    end_point[-1] = nums[i+1]
            elif next_start == -1:
                next_end = twodivide(end_point,nums[i+1][1])
                if next_end ==-2:
                    start_point = nums[i+1][0]
                    end_point = nums[i+1][1]
                
                else:
                    while end_point[0]<nums[i+1][1]:
                        end_point.pop(0)
                        start_point.pop(0)
                    end_point = [nums[i+1][1]] + end_point
                    start_point = [nums[i+1][0]] + start_point
#            else:
                
    return [[start_point],[end_point]]
                
        
nums = [[1,2],[4,8],[7,9]]
target = 2
#a = twodivide([2,8],target)
a = merge(self,nums)
print(a,target,nums)

#for i in range(max(nums)+1):
#    a = twodivide(nums,i)
#    print(a,i,nums)