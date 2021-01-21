# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:34:06 2020

@author: harshvardhan
"""



s = input("")
k = int(input())
ls = list(map(int,input().split()))

cost = 0
for i in range(len(s)):
    curr = ord(s[i])-97
    cost+=((i+1)*(ls[curr]))

i = i+1
for j in range(k):
    cost+= ((i+1)*(max(ls)))
    i+=1
    
print(cost)

