# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:40:24 2021

@author: 宋小兰
"""


import json
from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','neo4j'))
lines = []     #  第一步：定义一个列表， 打开文件
with open("清热药入药方剂完整属性_end.txt",'rt',encoding="utf-8") as f:  
    for row in f.readlines(): # 第二步：读取文件内容 
        if row.strip().startswith("//"):   # 第三步：对每一行进行过滤 
            continue
        lines.append(row)                  # 第四步：将过滤后的行添加到列表中.



count=0
for i in range(4900,5448):
    matcher=NodeMatcher(graph)
    n=matcher.match("方剂",id=i)
    for node in n:
        dict=json.loads(lines[count],strict=False)       #将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！
        #print(dict)
        
        node['所属分类']=dict['所属分类：']
        node['药用公用']=dict['药用公用：']
        node['功效主治']=dict['功效主治：']
        node['组成']=dict['组成：']
        node['方剂出处']=dict['方剂出处：']
        node['药材配方']=dict['药材配方：']
        node['方剂用法']=dict['方剂用法：']
        node['方剂附注']=dict['方剂附注：']
        graph.push(node)
        print(count)
        count=count+1