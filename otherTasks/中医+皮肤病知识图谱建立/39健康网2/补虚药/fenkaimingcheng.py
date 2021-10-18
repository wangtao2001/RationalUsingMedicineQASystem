# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:37:02 2021

@author: 宋小兰
"""


yaocais = []
bieming = []
for i in  open("名称.txt","r",encoding = "utf-8"):
    if '(' in i:
        name = i.split('(')
        #print(name)
        yaocais.append(name[0])
        #bieming.append(name[1])
        
    else:
        yaocais.append(i[:-1])
        #bieming.append("null")
with open("yaocai.txt",'w',encoding="utf-8") as f:     
    for j in yaocais:
        #print(j)
        f.write(j+'\n')