# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:40:07 2018

@author: ljc
"""
w = [0, 1, 4, 3, 1]   #n个物体的重量(w[0]无用)
p = [0, 1500, 3000, 2000, 2000]   #n个物体的价值(p[0]无用)
n = len(w) - 1   #计算n的个数
m = 4   #背包的载重量

x = []   #装入背包的物体，元素为True时，对应物体被装入(x[0]无用)
v = 0
#optp[i][j]表示在前i个物体中，能够装入载重量为j的背包中的物体的最大价值
optp = [[0 for col in range(m + 1)] for raw in range(n + 1)]

def knapsack_dynamic(w, p, n, m, x):
    #计算optp[i][j]
    for i in range(1, n + 1):       # 物品一件件来
        for j in range(1, m + 1):   # j为子背包的载重量，寻找能够承载物品的子背包
            if (j >= w[i]):         # 当物品的重量小于背包能够承受的载重量的时候，才考虑能不能放进去
                optp[i][j] = max(optp[i - 1][j], optp[i - 1][j - w[i]] + p[i])    # optp[i - 1][j]是上一个单元的值， optp[i - 1][j - w[i]]为剩余空间的价值
            else:
                optp[i][j] = optp[i - 1][j]

    #递推装入背包的物体,寻找跳变的地方，从最后结果开始逆推
    j = m
    for i in range(n, 0, -1):
        if optp[i][j] > optp[i - 1][j]:
            x.append(i)
            j = j - w[i]  
    print(optp)
    #返回最大价值，即表格中最后一行最后一列的值
    v = optp[n][m]
    return v
print ('最大值为：' + str(knapsack_dynamic(w, p, n, m, x)))
print ('物品的索引：',x)