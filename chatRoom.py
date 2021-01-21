# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 22:11:20 2020

@author: harshvardhan
"""

s1 = input()
s2 = "hello"
j = 0 
c = 0
flag = 1
for i in range(len(s1)):
    if s1[i]==s2[j]:
        j+=1
        c+=1
    if c==len(s2):
        print("YES")
        flag = 0
        break
if flag:
    print("NO")