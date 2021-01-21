# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 01:03:55 2020

@author: harshvardhan
"""




num = list(map(int,input().split()))
flag = 0
"""
for i in range(len(num)-1):
    if num[i]%2==0 and num[i]<num[-1]:
        num[i],num[-1] = num[-1],num[i]
        flag =1
        break

if flag==False:
    for i in range(len(num)-2,-1,-1):
        if num[i]%2==0:
            num[i], num[-1] = num[-1], num[i]
            flag = 1
            break
if flag:
    print(num)
else:
    print(-1)

  """  