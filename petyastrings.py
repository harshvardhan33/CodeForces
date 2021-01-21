# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 01:58:08 2020

@author: harshvardhan
"""

s1 = input().lower()
s2 = input().lower()

if s1==s2:
    print(0)
elif s1<s2:
    print(-1)
else:
    print(1)