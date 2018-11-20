# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:39:29 2018

@author: ljc
"""
def run_mn(m,n):
    results = []
    i = 1
    j = 1
    def run(i,j,m,n,result,results):
        print(result)
        while i< m or j<n:
            if j==n and i<m:
#                print(i,j)
                result.append([i,j])
                break
            i += 1
            run(i,j,m,n,result,results)
            j += 1
            run(i-1,j,m,n,result,results)
        if result not in result:
            results.append(result)
#        print(results)

    run(i,j,m,n,[],results)
    return len(results)
#def fib(n):
#   if n == 0 or n == 1:
#       return n
#   return fib(n−1)+fib(n−2)
a = run_mn(3,3)
print(a)