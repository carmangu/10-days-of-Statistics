#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:07:41 2018

@author: Noodle

https://www.hackerrank.com/challenges/s10-interquartile-range/problem
"""

n = int(input())
num = list(map(int, input().split()))
freq = list(map(int, input().split()))

data = []
for i in range(len(num)):
    for j in range(freq[i]):
        data.append(num[i])
data=sorted(data)

def median(size, ds):
    if size % 2 ==0:
        median = (ds[int(size/2)-1] + ds[int(size/2)])/2
    else:
        median = float(ds[int(size/2)])
    return(median)

size = int(len(data))
if n % 2 == 0:
    d1 = data[0: int(size/2)]
    d2 = data[int(size/2): size]
else: 
    d1 = data[0: int(size/2)]
    d2 = data[int(size/2)+1: size]

q1=median(len(d1), d1)
q3=median(len(d2), d2)

print(q3-q1)