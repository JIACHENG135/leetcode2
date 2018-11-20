# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:21:52 2018

@author: ljc
"""

def test_copy(a):
    key_a = [key for key in list(a.keys())]
    v_a = [value for value in list(a.values())]
    b_n = dict(zip(key_a,v_a))    
    b = dict(zip(a.keys(),a.values()))
    b_l = dict(zip(list(a.keys()),list(a.values())))
    print(a,b)
    print(a,b_l)
    print(a,b_n)
    a['a'].pop(0)
    print(a,b)
    print(a,b_l)
    print(a,b_n)
    