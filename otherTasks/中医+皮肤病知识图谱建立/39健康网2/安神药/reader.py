# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 20:27:44 2021

@author: 宋小兰
"""
textfile=open('安神药基本属性.txt','rt',encoding="utf-8")
list=[]
count=0
for line in textfile.readlines():
    list.append(line)
    count+=1
textfile.close()
print(count)
f2=open('基本属性2.txt','w',encoding="utf-8")
for i in range(0,count):
    if i%2 != 0:
        print(list[i])
        f2.write(list[i])
f2.close()

