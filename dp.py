# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:20:29 2018

@author: ljc
"""
def dp(w,p,m):
    n = len(p)
    unit = 1 # mass unit
    optp = [[0 for col in range(m)] for row in range(len(p))]
    print(optp)
    for i in range(len(p)):
        for j in range(m):
            s = i
            while unit*j>=max() and s>0:
                s -= 1 
                optp[i][j] = max()
                
                

for i in range(1, n + 1):       # 物品一件件来
    for j in range(1, m + 1):   # j为子背包的载重量，寻找能够承载物品的子背包
        if (j >= w[i]):         # 当物品的重量小于背包能够承受的载重量的时候，才考虑能不能放进去
            optp[i][j] = max(optp[i - 1][j], optp[i - 1][j - w[i]] + p[i])    # optp[i - 1][j]是上一个单元的值， optp[i - 1][j - w[i]]为剩余空间的价值
        else:
            optp[i][j] = optp[i - 1][j]

a = dp([1,4,3,1],[1500,3000,2000,2000],4)
