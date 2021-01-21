# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:23:48 2020

@author: harshvardhan
"""




s1 = "AEDFHR"
s2 = "ABCDFH"

n = len(s1)
m = len(s2)


dp = [[0 for i in range(n+1)]for j in range(m+1)]
ans = float("-inf")
for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
        if s1[i-1]==s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            ans = max(ans,dp[i][j])
        else:
            dp[i][j] = 0
            ans = max(ans,dp[i][j])
print(ans)
