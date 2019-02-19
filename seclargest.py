# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 23:11:31 2019

@author: Suneel
"""

n=int(input())
num_str_ar=input().strip().split()

num_ar=list(map(int,num_str_ar))
set_tmp=set(num_ar)
final_ar=list(set_tmp)
final_ar.sort()
print (final_ar[-2])