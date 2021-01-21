# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:53:30 2020

@author: harshvardhan
"""

n = int(input())
s = list(map(int,input().split()))
s_a = sum(s)//2
s_b = 0
c= 0
s.sort(reverse=True)
for i in range(len(s)):
    s_b+=s[i]
    c+=1
    if s_b>s_a:
        break
print(c)