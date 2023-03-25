# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:10:16 2023

@author: MD JOHIRUL ISLAM
"""

def re_fun(n):
    if n == 0:
        return 1
    else:
        return (5+5)+re_fun(n-1)
    
a = re_fun(10)
print(a)