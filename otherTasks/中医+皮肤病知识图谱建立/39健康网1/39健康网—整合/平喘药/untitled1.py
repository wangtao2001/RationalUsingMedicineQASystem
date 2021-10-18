# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:20:13 2021

@author: 独顽似鄙
"""
fangjis=[]
for i in  open("入药方剂名.txt","r",encoding = "utf-8"):
    if '：' in i:
        continue
    elif '的入药方剂' in i:
        continue
    elif i == '\n':
        continue
    else:
        i = i.replace('\n','')
        fangjis.append(i)
with open("入药方剂名—new.txt",'w',encoding="utf-8") as f:
    for j in fangjis:
        print(j)
        f.write(j+"\n")