# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:55:35 2018

@author: ljc
"""
import time
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        key = []
        values = []
        
        for i in range(len(s)-1):
            if s[i] not in key:
                value_temp = [i]
                key.append(s[i])
                k = len(s)-1
                    
                while k>i:
#                    print(k)
                    if s[k] == s[i]:
                        value_temp.append(k)
                    k -=1
            if len(value_temp)>=2:
                values.append(value_temp)

        dict_num = dict(zip(key,values))
        return dict_num
    def isPalindrome(self,s):
        while len(s)>1:
            if s[0]==s[-1]:
                return self.isPalindrome(s[1:-1])
            else:
                return False
        return True
    
    def cal_value_diff(self,dict_d):
        '''
        tacitly consent that dic_d.values len bigger than 2
        '''
        max_diff = []
        key = []
        for i in dict_d:
            max_diff.append(max(dict_d[i])-min(dict_d[i]))
            key.append(i)
        return dict(zip(key,max_diff))
    
    def track_back(self,s,b,c):
        x = max(c,key=c.get)
        copy_b = b.copy()
        while len(b[x])>=2:
            l = min(b[x])
            r = max(b[x])
            if self.isPalindrome(s[l:r+1]):
                return (s[l:r+1])
                break

    #        b[x] = b[x].pop(b[x].index(max(b[x])))
            max_b = b[x].index(max(b[x]))
            min_b = b[x].index(min(b[x]))
            b[x].pop(max_b)
            copy_b[x].pop(min_b)
            c = self.cal_value_diff(b)
            copy_c = self.cal_value_diff(copy_b)
            x = max(c,key=c.get)
            copy_x = max(copy_c,key=copy_c.get)
            if self.track_back(s,b,c) and self.track_back(s,copy_b,copy_c):
                if len(self.track_back(s,b,c))>len(self.track_back(s,copy_b,copy_c)):
                    return self.track_back(s,b,c)
                else:
                    return self.track_back(s,copy_b,copy_c)
            elif (not self.track_back(s,b,c)) and self.track_back(s,copy_b,copy_c):
                return self.track_back(s,copy_b,copy_c)
            elif (not self.track_back(s,copy_b,copy_c)) and self.track_back(s,b,c):
                return self.track_back(s,b,c)
            else:
                return False
        return False
                
if __name__ == '__main__':
    a=Solution()
    s = 'babad'
    b = a.longestPalindrome(s)
    c = a.cal_value_diff(b)
    if c:
        x = max(c,key=c.get)

    while len(b[x])>=2:
        l = min(b[x])
        r = max(b[x])
        if a.isPalindrome(s[l:r+1]):
            print(s[l:r+1])
            break
#        b[x] = b[x].pop(b[x].index(max(b[x])))
        max_b = b[x].index(max(b[x]))
        b[x].pop(max_b)
        c = a.cal_value_diff(b)
        x = max(c,key=c.get)
#        print(b[x],max_b,x)
#        time.sleep(2)
#    d.__next__()
#    print(b,c
    