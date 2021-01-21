# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:29:41 2020

@author: harshvardhan
"""




n,t = map(int,input().split())
s =list(input())
temp = s[:]
while t:
    t-=1
    for i in range(len(s)-1):
        if s[i]=='B' and s[i+1]=="G":
            temp[i],temp[i+1] = temp[i+1],temp[i]
    s = temp[:]

print("".join(s))