# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 12:13:02 2018

@author: ljc
"""

def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]
#
print(permute(1, ["a","b","c"]))
#print(permute(3, ["a","b","c"]))


def isHui(S):
    if len(S)<=1:
        return True
    elif S[0] == S[-1]:
        return isHui(S[1:-1])
    else:
        return False
    


    

def findNsum(l, r, target, N, result, results):
    if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
        return
    if N == 2: # two pointers solve sorted 2-sum problem
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif s < target:
                l += 1
            else:
                r -= 1
#    elif r-l + 1 == N:
#        results.append(nums)
    else: # recursively reduce N
        for i in range(l, r+1):
            if i == l or (i > l and nums[i-1] != nums[i]):
                findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

##    return results





def myfd(l,r,nums,target,N,result,results):
    if N<2 or r-l+1<N or nums[0]*N>target or nums[-1]*N<target:
        return
    if N == 2:
        while l<r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l],nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
    else:
        for i in range(l,r+1):
            if i == l or (i > 1 and nums[i-1] != nums[i]):
                myfd(i+1,r,nums,target - nums[i],N-1,result + [nums[i]],results)
                
#nums = [1,2,3,4,5,7,2,6,1]
#target  = 7;
#nums.sort()
#results = []
#myfd(0, len(nums)-1,nums, target, 4, [], results)
#print(results)

import copy
def mychose(Nums,k,index,result,results):
    if k == 1:
        for i in range(len(Nums)):
#            if result[-1]<Nums[i]:# this is the differen
            if list()
            results.append(result +[Nums[i]])
    else:
        for i in range(len(Nums)):
            Nums_temp = copy.copy(Nums)
            Nums_temp.pop(i)
            index = i
#            if (len(result)  == 0 or result[-1]<Nums[i]) and Nums[i]:
            mychose(Nums_temp,k-1,index,result+[Nums[i]],results)

result = []
results = []
nums = [1,2,3]
nums = list(set(nums))
nums.sort()
#diff = nums[0:-2]
mychose(nums,2,0,result,results)
print(list(set(results)))















#
def nchosek(nums,k):
    def test_x(x):
        if x == 1:
            return x
    return True
    




















