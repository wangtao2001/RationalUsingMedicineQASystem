# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 09:12:08 2021

@author: 宋小兰
"""


import json
lines = []     #  第一步：定义一个列表， 打开文件
with open("清热药入药方剂完整属性_end.txt",'rt',encoding="utf-8") as f:  
    for row in f.readlines(): # 第二步：读取文件内容 
        if row.strip().startswith("//"):   # 第三步：对每一行进行过滤 
            continue
        lines.append(row)                   # 第四步：将过滤后的行添加到列表中.
count=0

for line in lines:
    dict=json.loads(lines[1],strict=False)       #将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！
    count+=1
    print(count)
    print(dict.keys())
#print(dict['【别名】'])
    