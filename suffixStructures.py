# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:07:56 2021

@author: harshvardhan
"""

s = "automaton"
t = "tomat"
if t in s and len(t)<len(s):
    print("automaton")
elif sorted(s)==sorted(t):
    print("array")
    
    