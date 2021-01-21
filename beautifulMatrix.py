# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:42:26 2020

@author: harshvardhan
"""



n = 5
mat = []
for i in range(n):
    res = list(map(int,input().split()))
    mat.append(res)

a,b =0,0
for i in range(n):
    for j in range(n):
        if mat[i][j]==1:
            a = i+1
            b = j+1
            break
    
print(abs(3-a)+abs(3-b))