# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:25:28 2021

@author: 宋小兰
"""


import re
textfile=open('入药方剂.txt','rt',encoding="utf-8")
list=[]
for line in textfile.readlines():
    list.append(line)
textfile.close()
'''
for i in list:
    print(i)
'''
count=0
f2=open('入药方剂_name.txt','w',encoding="utf-8")
for line in list:
    count=count+1
    #print(i[-6:-1])
    if "{" in line:
        print(list[count-2])    
        f2.write(list[count-2])
f2.close()
