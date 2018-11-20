# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:16:20 2018

@author: ljc
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:10:56 2018

@author: ljc
"""
import copy
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):
            while len(s)>1:
                if s[0]==s[-1]:
                    return isPalindrome(s[1:-1])
                else:
                    return False
            return True
        def cal_value_diff(dict_d):
            max_diff = []
            key = []
            for i in dict_d:
                max_diff.append(max(dict_d[i])-min(dict_d[i]))
                key.append(i)
            return dict(zip(key,max_diff)) 
        def longestPalindrome_ljc(s):
            key = []
            values = []
            for i in range(len(s)-1):
                if s[i] not in key:
                    value_temp = [i]
                    key.append(s[i])
                    k = len(s)-1
                    while k>i:
                        if s[k] == s[i]:
                            value_temp.append(k)
                        k -=1
                if len(value_temp)>=2:
                    values.append(value_temp)
            dict_num = dict(zip(key,values))
            return dict_num
        def track_back(s,b,c):
            x = max(c,key=c.get)
            copy_b = copy.deepcopy(b)
            while len(b[x])>=2:
                l = min(b[x])
                r = max(b[x])
                if isPalindrome(s[l:r+1]):
                    return s[l:r+1]
                    break
                max_b = b[x].index(max(b[x]))
                min_b = copy_b[x].index(min(copy_b[x]))
                b[x].pop(max_b)
                copy_b[x].pop(min_b)
                c = cal_value_diff(b)
                copy_c = cal_value_diff(copy_b)
                res1 = track_back(s,b,c)
                res2 = track_back(s,copy_b,copy_c)
                if res1 and res2:
                    if len(res1)>len(res2):
                        return res1
                    else:
                        return res2
                elif res2:
                    return res2
                elif res1:
                    return res1
    
            return s[0]
        if len(s) <= 1:
            return s
        else:
            b = longestPalindrome_ljc(s)
            c = cal_value_diff(b)
            if c:
                return track_back(s,b,c)

            elif len(s)>=2:
                return s[0]
            else:
                return ''
                
        
        
    
a = Solution()
b = a.longestPalindrome("babaddtattarrattatddetartrateedredividerb")
print(b)



