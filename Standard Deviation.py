#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:13:41 2018

@author: Jingwen

https://www.hackerrank.com/challenges/s10-standard-deviation/problem
"""

n = int(input())
num = list(map(int, input().split()))
mean = sum(num)/n
import math 

sum=0
for i in range(len(num)):
    sum = sum + (num[i] - mean)**2
    
print(round(math.sqrt(sum/n),1))