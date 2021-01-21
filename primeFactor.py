# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 22:48:52 2021

@author: harshvardhan
"""


n = 50
primes = [-1 for i in range(n+1)]

for i in range(2,len(primes)):
    if primes[i]==-1:
        primes[i]=i
        curr = i*i
        for j in range(curr,n+1,i):
            primes[j] = i
        