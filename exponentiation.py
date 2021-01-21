# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 22:42:53 2021

@author: harshvardhan
"""



a = 2
p = 10
res =1
while p>0:
    if p%2!=0:
        res = res*a
    a = a*a
    p = p//2