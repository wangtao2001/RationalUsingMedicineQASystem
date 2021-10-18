# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:25:28 2021

@author: 宋小兰
"""


import re
textfile=open('清热药药名_方剂.txt','rt',encoding="utf-8")
list=[]
for line in textfile.readlines():
    list.append(line)
textfile.close()
'''
for i in list:
    print(i)
'''

f2=open('清热药药名_name.txt','w',encoding="utf-8")
f3=open('清热药方剂名_name.txt','w',encoding="utf-8")
for line in list:
    #print(i[-6:-1])
    if "{" in line:
        print(line)    
        f2.write(line)
    else:
        f3.write(line)
f2.close()
f3.close()
