class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        if len(nums) == 1:
            return nums[0]
        else:

            def cal_product(nums,key,value):
                if nums in key:
                    return value[key.index(nums)]
                else:
                    k = 0
                    r = len(nums)
                    prod = 1
                    while k<r:
                        prod *= nums[k]
                        k += 1
                    key.append(nums)
                    value.append(prod)
                return prod

            def count_minus(nums):
                minus = [0]*len(nums)
                for i in range(len(nums)):
                    if nums[i]<0:
                        minus[i] = -1
                        nums[i] = -nums[i]
                return minus,nums
            def permutation_01(n,k):
                first = [1 for i in range(k)] + [0 for i in range(len(n)-k)]
                last = [0 for i in range(len(n)-k)] + [1 for i in range(k)]
                permu = []

                while first != last:
                    permu.append(list(filter(lambda x: x!=0,list(map(lambda i,j:i*j,first,n)))))
                    counter = 0

                    for i in range(len(n)-1):
                        if first[i] == 1:
                            counter += 1
                            if first[i+1]==0:
                                first[i],first[i+1] = first[i+1],first[i]
                                first[0:i] = [1 for j in range(counter-1)] + [0 for j in range(i-counter+1)]
                                break
                permu.append(list(filter(lambda x: x!=0,list(map(lambda i,j:i*j,last,n)))))
                return permu
            def permu2list(A,permu):
                permu = [0]+permu+[len(A)+1]
                res = []
                for i in range(len(permu)-1):
                    res.append(A[permu[i]:permu[i+1]])
                return res


            def find_index(str_all,str_in,str_con):
                first_ind = [i for i in range(len(str_all)) if str_all[i]==str_in[0]]
                print('first_ind',first_ind)
                ans=[]
                for j in first_ind:

                    i = j
                    while i < len(str_all)-1:            
                        while str_all[i] == str_in[0]:
                            if len(str_in) == 1:
                                if i not in ans:
                                    ans.append(i)
                                    print('ans',ans)
                                break
                            str_in = str_in[1:]
                            i += 1
                        str_in = str_con
                        i += 1
                ans = [first_ind[0]] + ans  

                return ans

            def find_zero(nums):
                res = []
                nums_res = []
                for i in range(len(nums)):
                    if nums[i]==0:

                        res.append(i)
                        if len(res) == 1:
                            if not nums[:i]:
                                pass
                            else:
                                nums_res.append(nums[:i])
                        else:
                            if not nums[res[-2]+1:i]:
                                pass
                            else:
                                nums_res.append(nums[res[-2]+1:i])
    #                    print(res,'res')    
    #            print(nums_res,'nums_res')
                if res:
                    if nums[res[-1]+1:]:
                        nums_res.append(nums[res[-1]+1:])
                    nums_res.append([0])
                if not nums_res:
                    return [nums]
                return nums_res

            def find_max_value(nums):
                key = []
                value = []
                for l in range(len(nums)):     
                    a = permutation_01([k for k in range(1,len(nums))],l)
                    for i in a:
                        c = permu2list(nums,i)
                        for j in c:

                            cal_product(j,key,value)


                return max(value)


    #        print(find_max_value([0]))
            nums_res = find_zero(nums)
            print(nums_res)
            max_v = float('-inf')
            for i in range(len(nums_res)):
                max_v = max(find_max_value(nums_res[i]),max_v)
            return max_v
        
a = Solution()
nums = [0,-2,0]
#res = permu2list(nums,)
b = a.maxProduct(nums)

#print(b.index(max(b)))
print(b)