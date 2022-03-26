# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 11:57:54 2022

@author: user
"""
def is_divisible(n):
    nd = n
    s =0
    while nd >0:
        s += nd%10//1
        nd /=10
        
    return (n%s) ==0
