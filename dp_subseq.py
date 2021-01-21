# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:12:26 2020

@author: harshvardhan
"""



s1 = "AEDFHR"
s2 = "ABCDGH"

n = len(s1)
m = len(s2)


dp = [[0 for i in range(n+1)]for j in range(m+1)]

for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
        if s1[i-1]==s2[j-1]:
            dp[i][j] = max(dp[i-1][j-1]+1,dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
print(dp[-1][-1])

i = len(dp)-1
j = len(dp[0])-1
print(i,j)
while i>0 and j>0:
    if s1[i-1]==s2[j-1]:
        print(s1[i-1])
        i-=1
        j-=1
    elif dp[i-1][j]>dp[i][j-1]:
        i-=1
    else:
        j-=1
        
   
