# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:14:17 2018

@author: ljc
"""

def find_index(str_all,str_in,str_con):
#        str_in_len = len(str_in)
    first_ind = [i for i in range(len(str_all)) if str_all[i]==str_in[0]]
    ans=[]
    for j in first_ind:

        i = j
        while i < len(str_all):            
            while str_all[i] == str_in[0]:
                if len(str_in) == 1:
                    if i not in ans:
                        ans.append(i)
                    break
                str_in = str_in[1:]
                i += 1
            str_in = str_con
            i += 1
    return ans