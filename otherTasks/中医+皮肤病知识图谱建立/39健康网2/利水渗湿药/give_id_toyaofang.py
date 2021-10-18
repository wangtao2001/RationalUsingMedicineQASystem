# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:25:28 2021

@author: 宋小兰
"""


import re
textfile=open('yao_fangji_name.txt','rt',encoding="utf-8")
list=[]
for line in textfile.readlines():
    list.append(line)
textfile.close()
'''
for i in list:
    print(i)
'''
count=0
f2=open('you_yaoji_yao.txt','w',encoding="utf-8")
#f3=open('chunyaoji.txt','w',encoding="utf-8")
for line in range(1,711):
    if "{"  in list[line-1] and "{" not in list[line]:
        f2.write(list[line-1])
    elif "{" not in list[line]:
        f2.write("null"+"\n")
        #f3.write(list[line])
        print(list[line])
        count=count+1
        print(count)
    else:
        print("wu")
f2.close()
#f3.close()
       
