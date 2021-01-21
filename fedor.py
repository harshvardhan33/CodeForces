# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 23:16:20 2020

@author: harshvardhan
"""

n,m,k = map(int,input().split())
res = []
while m+1:
    m-=1
    temp = int(input())
    res.append(temp)
fed = res[-1]
del res[-1]
c=0 
for i in range(len(res)):
    temp = bin(fed^res[i])[2:].count("1")
    if temp<=k:
        c+=1    
print(c)