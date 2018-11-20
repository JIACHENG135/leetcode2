def cbSum(nums,l,r,N,target,result=[],results=[]):
#    print(l,r,N)
    if r - l + 1 <N or target > N*nums[r] or target < N*nums[l] or N<2:
        return
    if N==2:
        while l<r:
#            print(l,r)
            s =nums[r] + nums[l];
            if s ==target:
                print(results)
                results.append(result + [nums[l],nums[r]])
                l += 1
                while l<r and nums[l-1] ==nums[l]:
                    l +=1
            elif s<target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(l,r+1):
            if i==l or (i>1 and nums[i-1] != nums[i]): 
                return cbSum(nums,i+1,r,N-1,target - nums[i],result+[nums[i]],results) 
    return results

def fourSum( nums, target):
    if target in nums:
        results= [target]
    else:
        results = []
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
        else: # recursively reduce N
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

    nums.sort()
    for i in range(1,len(nums)+1):
        findNsum(0, len(nums)-1, target, i, [], results)
    return results
a = fourSum([1,1],2)
print(a)