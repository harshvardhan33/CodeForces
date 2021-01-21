# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 22:25:59 2020

@author: harshvardhan
"""



n,m = map(int,input().split())

mx = ((n-(m-1))*(n-(m-1)-1))//2
sz = n//m
rem = n%m
mn = (rem*(sz+1)*(sz))//2 + ((m-rem)*(sz)*(sz-1))//2

print(mn,mx)