# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:09:42 2021

@author: 宋小兰
"""


textfile=open('入药方剂.csv','rt',encoding="utf-8")
list=[]
count=0
for line in textfile.readlines():
    list.append(line)
textfile.close()
print(count)
f2=open('入药方剂2.txt','w',encoding="utf-8")
for i in list:
    if i[0] == "{":
        print(i)
        f2.write(i)
f2.close()