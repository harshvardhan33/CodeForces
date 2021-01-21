# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 01:50:59 2020

@author: harshvardhan
"""

s = input()
s = s.lower()
vowel = "aeiouy"
i = 0
s = list(s)
while i<len(s):
    if s[i] in vowel:
        del s[i]
    else:
        i+=1
ans = "."+".".join(s)
print(ans)