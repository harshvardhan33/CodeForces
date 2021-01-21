# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 19:16:41 2021

@author: harshvardhan
"""



n,pos1,pos2 = map(int,input().split())
params = list(map(int,input().split()))
arr = [i+1 for i in range(n)]
first = arr[:]
if arr[pos2-1]==pos1:
    print(0)
else:
    flag1 = 1
    count = 0
    while True:
        if arr[pos2-1]==pos1:
            break
        temp = [0 for i in range(n)]
        if flag1:
            flag1=0
            count+=1
            for i in range(len(params)):
                temp[params[i]-1] = arr[i]
            arr = temp[:]            
        else:
            if arr[:]==first[:]:
                count = -1
                break
            for i in range(len(params)):
                temp[params[i]-1] = arr[i]
            arr = temp[:]
            count+=1            
    print(count)


