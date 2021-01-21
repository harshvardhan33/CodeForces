# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 22:34:33 2021

@author: harshvardhan
"""


def dfs(curr,depth,end):
    if visited[curr]==1:
        return -1
    elif curr==end:
        return depth
    visited[curr]=1
    return dfs(graph[curr],depth+1,end)



n,pos1,pos2 = map(int,input().split())
params = list(map(int,input().split()))
graph = {}

for i in range(len(params)):
    graph[i+1] = params[i]
    

visited = [0 for i in range(n+1)]

print(dfs(pos1,0,pos2))