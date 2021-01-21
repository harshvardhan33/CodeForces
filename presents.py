# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:10:58 2020

@author: harshvardhan
"""



n = int(input())
arr = list(map(int,input().split()))
ans = [None for i in range(n)]


for i in range(len(arr)):
    ans[arr[i]-1] = i+1
print(*ans)