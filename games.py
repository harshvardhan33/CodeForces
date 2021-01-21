# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 23:16:12 2021

@author: harshvardhan
"""

n = int(input())
dc1 = {}
dc2 = {}
while n:
    n-=1
    a,b = map(int,input().split())
    if a not in dc1:
        dc1[a] = 1
    elif a in dc1:
        dc1[a]+=1
    if b not in dc2:
        dc2[b] = 1
    elif b in dc2:
        dc2[b]+=1
    if a not in dc2:
        dc2[a] = 0
    if b not in dc1:
        dc1[b]=0

ans = 0
for i,j in dc1.items():
    ans+=dc1[i]*dc2[i]

print(ans)
        
    