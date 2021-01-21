# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:27:52 2020

@author: harshvardhan
"""


import random
import math

s1 = "abc"
s1 = list(s1)
n = len(s1)
final = []
while len(final)!=(math.factorial(n)):
    temp=""
    while len(temp)!=n:
        x = random.choice(s1)
        if x in temp:
            continue
        else:
            temp+=x
    if temp not in final:
        final.append(temp)

for i in sorted(final):
     print(i)


