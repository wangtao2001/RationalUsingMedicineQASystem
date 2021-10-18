# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:40:36 2021

@author: 宋小兰
"""


import re
textfile=open('yao_fangji_name.txt','rt',encoding="utf-8")
list=[]
for line in textfile.readlines():
    list.append(line)
textfile.close()
f3=open('chunyaoji.txt','w',encoding="utf-8")
for line in range(0,506):
    if "{" not in list[line]:
        f3.write(list[line])
    else:
        print("wu")
f3.close()