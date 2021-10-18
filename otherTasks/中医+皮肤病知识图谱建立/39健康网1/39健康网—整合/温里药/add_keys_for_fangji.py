# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:33:14 2021

@author: 宋小兰
"""


import json
lines = []     #  第一步：定义一个列表， 打开文件
with open("清热药入药方剂属性_end.txt",'rt',encoding="utf-8") as f:  
    for row in f.readlines(): # 第二步：读取文件内容 
        if row.strip().startswith("//"):   # 第三步：对每一行进行过滤 
            continue
        lines.append(row)                   # 第四步：将过滤后的行添加到列表中.
count=0
dict_list=[]
'''
//确定一个方剂一共应该有多少属性
for line in lines:
    dict=json.loads(line,strict=False)       #将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！
    #count+=1
    #print(count)
    #print(dict)
    for i in dict.keys():
        if i in dict_list:
            continue
        else:
            dict_list.append(i)
print(dict_list)
'''
for line in lines:
    dict=json.loads(line,strict=False)       #将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！
    count+=1
    print(count)
    #print(dict)
    keys_list=['所属分类：', '药用公用：', '功效主治：', '组成：', '方剂出处：', '药材配方：', '方剂用法：', '方剂附注：']
    for i in keys_list:
        if i in dict.keys():
            continue
        else:
            dict[i]="null"
    #print(dict)
    dict_list.append(str(dict))
for j in dict_list:
    print(j)
    with open("清热药入药方剂完整属性_end.txt",'a',encoding="utf-8") as f2:
        f2.write(j+'\n')
    f2.close()