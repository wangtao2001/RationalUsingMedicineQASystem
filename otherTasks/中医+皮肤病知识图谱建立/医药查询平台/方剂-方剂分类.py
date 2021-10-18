# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:07:16 2021

@author: 宋小兰
"""
from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','qazplm-55454'))
list1=[]
with open("医药查询平台\\有分类的方剂.txt",encoding="utf-8") as f:  
        for row in f.readlines():
            row=row.strip()
            dict2 = row.split('《',1)
            #print(dict2[0])
            list1.append(dict2[0])

list2=[]
with open("医药查询平台\\方剂分类-作为节点.txt",encoding="utf-8") as f:  
        for row1 in f.readlines():
            row1=row1.strip()
            list2.append(row1)
            
#创建分类节点
for i in list2:
    try:
        node=Node("方剂分类", 方剂分类名称=i)
        graph.create(node)
    except:
        print("该节点已经存在")


matcher=NodeMatcher(graph)        
#创建关系
for j in range(0,14352):
    m=matcher.match("方剂", 方剂名称=list1[j])
    n=matcher.match("方剂分类", 方剂分类名称=list2[j])
    for node in m:
        print(dict(node)['方剂名称'])
        for node1 in n:
            print(dict(node1)['方剂分类名称'])
            n_m=Relationship(node,"所属分类",node1)
            graph.create(n_m)
    