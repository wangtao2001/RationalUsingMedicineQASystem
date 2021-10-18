# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 16:25:22 2021

@author: 宋小兰
"""

#首先引入该方法
from collections import Counter
from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','qazplm-55454'))

#创建方剂节点
name=[]
with open("医药查询平台\\fangjiname_new.txt",'rt',encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        #print(i)
        node=Node("方剂", 方剂名称=row)
        graph.create(node)
    
#创建属性

lines=[]
with open("医药查询平台\\shortDict完整属性.txt",'rt',encoding="utf-8") as f:  
    for row1 in f.readlines():
        if row1.strip().startswith("//"):   # 第三步：对每一行进行过滤 
            continue
        lines.append(row1)



lines2=[]
with open("医药查询平台\\infoDict完整属性.txt",'rt',encoding="utf-8") as f:  
    for row2 in f.readlines():
        if row2.strip().startswith("//"):   # 第三步：对每一行进行过滤 
            continue
        lines2.append(row2)


count=0
matcher=NodeMatcher(graph)
n=matcher.match("方剂")
#dict3={'注意事项':'null','方剂别名':'null','各家论述':'null','方剂歌诀':'null','加减化裁':'null','方剂鉴别':'null','趣味记忆':'null','方剂方义':'null'}
for node in n:
    dict1=eval(lines[count])
    dict2=eval(lines2[count])
    node['方剂别名']=dict1['别名']
    node['方剂出处']=dict1['出处']
    node['方剂歌诀']=dict2['歌诀']
    node['方剂组成']=dict2['组成']
    node['方剂用法']=dict2['方剂用法']
    node['功效主治']=dict2['功用']+'；'+dict2['主治']
    node['加减化裁']=dict2['加减化裁']
    node['药材配方']=dict2['药材配方']
    node['药用公用']=dict2['药用公用']
    node['方剂附注']=dict2['方剂附注']
    node['方剂制法']=dict2['制法']
    node['方剂鉴别']=dict2['化裁方之间的鉴别']
    node['趣味记忆']=dict1['趣味记忆']
    node['方剂方义']=dict2['方义']
    node['各家论述']=dict2['各家论述']
    node['注意事项']=dict2['使用注意']+'；'+dict2['注意事项']
    graph.push(node)
    print(count)
    count=count+1 