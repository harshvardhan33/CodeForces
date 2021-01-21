# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:04:26 2020

@author: harshvardhan
"""




n = 10**6
primes = [1 for i in range(10**6+10)]
tprime = {}    
for i in range(2,n):
    if primes[i]==1:
        tprime[i*i]=1
        k = i
        for j in range(i*i,n+10,k):
            primes[j]=0    

    
num = int(input())
arr = list(map(int,input().split()))
for i in arr:
    if i in tprime:
        print("YES")
    else:
        print("NO")