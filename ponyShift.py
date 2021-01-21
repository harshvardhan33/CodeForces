# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:31:00 2021

@author: harshvardhan
"""


n = int(input())
nums = list(map(int,input().split()))
res = -1
if sorted(nums)==nums:
    res = 0
else:
    brk = 0
    for i in range(len(nums)-1):
        if nums[i]<=nums[i+1]:
            continue
        else:
            brk=i+1
            break
    if nums[-1]<=nums[0] and sorted(nums[brk:])==nums[brk:]:
        res = len(nums)-brk
print(res)


