# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:05:13 2021

@author: harshvardhan
"""
s = input().strip(',')
ans = None 
if s=="{}":
    ans=0
else:
    s = s[1:-1].split(",")
    s = set([s[i].strip() for i in range(len(s))])
print(ans)
