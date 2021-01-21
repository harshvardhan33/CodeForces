# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:13:53 2020

@author: harshvardhan
"""
n = int(input())
arr = list(map(int,input().split()))
left = 0
right = 0
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        left = i
        break

for i in range(len(arr)-1,0,-1):
    if arr[i]<arr[i-1]:
        right = i
        break
temp = arr[:left]+arr[left:right+1][::-1]+ arr[right+1:]
if temp==sorted(arr):
    print("yes")
    print(left+1,right+1)
else:
    print("no")