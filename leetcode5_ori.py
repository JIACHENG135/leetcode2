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
        if len(s) <= 1:
            return s
        else:
            b = self.longestPalindrome_ljc(s)
            c = self.cal_value_diff(b)
            if c:
                return self.track_back(s,b,c)

            elif len(s)>=2:
                return s[0]
            else:
                return ''
                
    def isPalindrome(self,s):
        while len(s)>1:
            if s[0]==s[-1]:
                return self.isPalindrome(s[1:-1])
            else:
                return False
        return True
    
    

    def cal_value_diff(self,dict_d):
        max_diff = []
        key = []
        for i in dict_d:
            max_diff.append(max(dict_d[i])-min(dict_d[i]))
            key.append(i)
        return dict(zip(key,max_diff)) 
    def longestPalindrome_ljc(self, s):
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
    def track_back(self,s,b,c):
        x = max(c,key=c.get)
        copy_b = copy.deepcopy(b)
        while len(b[x])>=2:
            l = min(b[x])
            r = max(b[x])
            if self.isPalindrome(s[l:r+1]):
                return s[l:r+1]
                break
            max_b = b[x].index(max(b[x]))
            min_b = copy_b[x].index(min(copy_b[x]))
            b[x].pop(max_b)
            copy_b[x].pop(min_b)
            c = self.cal_value_diff(b)
            copy_c = self.cal_value_diff(copy_b)
#            print('both right',self.track_back(s,b,c),self.track_back(s,copy_b,copy_c))
            res1 = self.track_back(s,b,c)
            res2 = self.track_back(s,copy_b,copy_c)
#            if self.track_back(s,b,c) and self.track_back(s,copy_b,copy_c):
#                if len(self.track_back(s,b,c))>len(self.track_back(s,copy_b,copy_c)):
#                    return self.track_back(s,b,c)
#                else:
#                    return self.track_back(s,copy_b,copy_c)
#            elif self.track_back(s,copy_b,copy_c):
##                (not self.track_back(s,b,c)) and 
#                return self.track_back(s,copy_b,copy_c)
#            elif self.track_back(s,b,c):
##                (not self.track_back(s,copy_b,copy_c)) and 
#                return self.track_back(s,b,c)
#            else:
#                return False
            if res1 and res2:
                if len(res1)>len(res2):
                    return res1
                else:
                    return res2
            elif res2:
#                (not self.track_back(s,b,c)) and 
                return res2
            elif res1:
#                (not self.track_back(s,copy_b,copy_c)) and 
                return res1

        return s[0]
    

a = Solution()
b = a.longestPalindrome("babaddtattarrattatddetartrateedredividerb")
print(b)



