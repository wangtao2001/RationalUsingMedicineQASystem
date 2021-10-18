# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:01:56 2021

@author: 宋小兰
"""


from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','neo4j'))

bingming=[]
with open("无属性皮肤病.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        rowDict=row.split(':')
        bingming.append(rowDict[1])

dingyi=[]        
with open("简介.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        dingyi.append(row)
bingyibingji=[]
with open("病因病机.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        bingyibingji.append(row)
bingzhengtezheng=[]
with open("临床表现.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        bingzhengtezheng.append(row)
        
matcher=NodeMatcher(graph)
for i in range(0,44):
    n=matcher.match("皮肤病",皮肤病名称=bingming[i])
    for node in n:
        #print(dict(node)['皮肤病名称'])
        node['皮肤病定义']=dingyi[i]
        node['皮肤病病因病理']=bingyibingji[i]
        node['皮肤病症状特点']=bingzhengtezheng[i]
        graph.push(node)
 