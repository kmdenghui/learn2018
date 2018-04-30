#!/usr/bin/env python
# coding=utf-8
# Created by denghui on 2018/4/12.
import math
import sys
count_cir=0
count_rec=0

def circle(r):
    'calculate the area of a circle'
    global count_cir
    count_cir+=1
    return math.pi*r**2

def rec(x,y):
    global count_rec
    return x*y



if  __name__=='__main__':
    print('the command line arguments are:')
    for i in sys.argv:
        print(i)