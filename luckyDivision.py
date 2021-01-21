# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:50:06 2020

@author: harshvardhan
"""




n = 1000
arr = [0 for i in range(n+1)]
for i in range(1,n+1):
    curr =list(set(str(i)))
    if (curr==['4','7'] or curr==['4'] or curr==['7']):
        arr[i] = 1

num = int(input())
if arr[num]==1:
    print("YES")
else:
    flag = 0
    for i in range(1,len(arr)):
        if arr[i]==1 and num%i==0:
            flag = 1
            break
    if flag:
        print("YES")
    else:
        print("NO")
            