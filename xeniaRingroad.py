# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:55:51 2020

@author: harshvardhan
"""

n,m = map(int,input().split())
arr = list(map(int,input().split()))
res = 1
cost = 0
for i in range(len(arr)):
    t = (arr[i]-res)%n
    res = arr[i]
    cost+=t

print(cost)