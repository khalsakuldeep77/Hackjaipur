# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:29:22 2020

@author: USER
"""
import math
f = math.factorial

answer=[]
result=[]
final=0
count=0
t=int(input())
for i in range(t):
    listt=[int(i) for i in input().split()]
    answer.append(listt)
for i in range(len(answer)):
    distance=math.sqrt(answer[i][0]**2+answer[i][1]**2)
    t=distance/answer[i][2]
    result.append(t)
resultset=set(result)
if(t==1):
  final=0
else:  
  for i in resultset:
      count=result.count(i)
      if(count==1):
        final=final+0
      else:
        final=final+(f(count)//f(2)//f(count-2))
print(final)     