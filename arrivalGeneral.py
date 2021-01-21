# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:17:22 2020

@author: harshvardhan
"""



n = int(input())
arr = list(map(int,input().split()))

mn = float("inf")
mn_idx = 0
mx = float("-inf")
mx_idx = 0
for i in range(len(arr)):
    if arr[i]<=mn:
        mn_idx  = i
        mn = arr[i]
    if arr[i]>mx:
        mx_idx = i
        mx = arr[i]
if mx_idx>mn_idx:    
    mn_idx = mn_idx+1
print(mx_idx+n-mn_idx-1)