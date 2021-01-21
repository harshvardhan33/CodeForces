# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 19:16:50 2021

@author: harshvardhan
"""



n = int(input())
a,b,c = 0,0,0
for i in range(n):
    t1,t2,t3 = map(int,input().split())
    a+=t1
    b+=t2
    c+=t3

if a==0 and b==0 and c==0:
    print("YES")
else:
    print("NO")
