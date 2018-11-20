# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:28:03 2018

@author: ljc
"""
def ifchange(result =[]):
    a = 0
    b = 0

    def test(a,b,result):
        a = a +1
        result.append(1)
    test(a,b,result)
    return result
#    print(a,b,result)
a = ifchange()
print(a)