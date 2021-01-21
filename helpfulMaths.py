# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 02:02:27 2020

@author: harshvardhan
"""

s = input()
s = sorted(s)
c = s.count("+")
ans = ""
for i in range(c,len(s)):
    ans=ans+s[i]+"+"

print(ans[:-1])