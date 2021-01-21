# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 23:52:53 2021

@author: harshvardhan
"""

s = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB" 
res = ""
flag = 1
temp = s.split("WUB")
for i in temp:
    if i!="":
        if flag:
            res+=i
            flag=0
        else:
            res+=" "+i
print(res)
