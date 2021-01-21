# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:25:40 2021

@author: harshvardhan
"""
import numpy as np
f1,f2 = map(int,input().split())
n = int(input())
m = np.array([[0,-1],[1,1]])
res = np.array([[1,0],[0,1]])
a = np.array([f1,f2]).reshape(1,-1)
b = n-2
while b:
    if b&1:
        res = np.dot(res,m)
    m = np.dot(m,m)
    b>>=1
ans = np.dot(a,m)[0][0]
print(ans%(10**9+7))