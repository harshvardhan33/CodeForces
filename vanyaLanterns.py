# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:37:58 2020

@author: harshvardhan
"""

n,l = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
ans = max(arr[0],l-arr[n-1])*2
for i in range(len(arr)-1):
    ds = arr[i+1]-arr[i]
    ans = max(ans,ds)
    
print(f"{ans/2:.9f}")