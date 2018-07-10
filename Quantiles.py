#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:23:34 2018

@author: Issac Noodle 

# question 
https://www.hackerrank.com/challenges/s10-quartiles/problem
"""
# correct answer in python3
n = int(input())
num = sorted(list(map(int, input().split())))

def quatr (n, num):
    if n % 2 ==0:
        quatr = (num[int(n/2) -1] + num[int(n/2)]) / 2
    else:
        quatr= (num[int(n/2)])
    return int(quatr)

if n % 2 == 0:
    d1 = num[0:int(n/2 )]
    d2 = num[int(n/2): n]

else :
    d1 = num[0: int(n/2)]
    d2 = num[int(n/2) + 1: n]

print(quatr(len(d1),d1))
print(quatr(n,num))
print(quatr(len(d2),d2))


# first try: missed one case in python 2
def quatr():
    n=int(raw_input())
    intg=sorted(map(int, raw_input().split()))
    if (len(intg) % 2) == 0: 
        q2 = (intg[n/2 -1] + intg[n/2])/2
        q1 = (intg[n/4 -1] + intg[n/4])/2
        q3 = (intg[3*n/4 -1] + intg[3*n/4])/2
    else :
        q2 = intg[(n-1)/2]
        q1 = (intg[(n-1)/4 - 1] + intg[(n-1)/4] )/2
        q3 = (intg[3*((n-1)/4)] + intg[3*((n-1)/4)+1])/2
    print (q1)
    print (q2)
    print (q3)
    
if __name__ == '__main__':
    quatr()
