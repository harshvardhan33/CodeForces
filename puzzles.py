# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:52:52 2021

@author: harshvardhan
"""



n1,n2 = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = float("inf")
for i in range(len(arr)-n1+1):
    ans = min(ans,arr[i+n1-1]-arr[i])
print(ans)