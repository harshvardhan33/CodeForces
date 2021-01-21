# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 01:46:21 2020

@author: harshvardhan
"""

n = int(input())
while n:
    n-=1
    word = input()
    if len(word)>10:
        print(word[0]+str(len(word))+word[-1])
    else:
        print(word)