# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:08:21 2021

@author: harshvardhan
"""
import math
r,x1,y1,x2,y2 = map(int,input().split())

ans = math.ceil(math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))/(2*r))
print(ans)