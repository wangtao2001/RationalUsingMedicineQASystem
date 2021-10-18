# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:57:42 2021

@author: 宋小兰
"""
from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','neo4j'))

matcher=NodeMatcher(graph)
dict2={'方剂制法':'null','方剂别名':'null','加减化裁':'null','方剂附注':'null','药用公用':'null','方剂出处':'null','药材配方':'null','各家论述':'null','方剂歌诀':'null','方剂鉴别':'null','趣味记忆':'null','方剂方义':'null'}
with open("效验方.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        row=eval(row)
        #print(row.keys())
        try:
            node=Node("方剂", 方剂名称=row['方名'],功效主治=row['功效'],药材配方=dict2['药材配方'],
                      方剂别名=dict2['方剂别名'],方剂歌诀=dict2['方剂歌诀'],方剂出处=dict2['方剂出处'],
                      方剂组成=row['组成'],药用公用=dict2['药用公用'], 方剂附注=dict2['方剂附注'],
                      方剂制法=dict2['方剂制法'],方剂鉴别=dict2['方剂鉴别'],趣味记忆=dict2['趣味记忆'],
                      方剂方义=dict2['方剂方义'],各家论述=dict2['各家论述'],加减化裁=row['加减'],
                      方剂用法=row['用法'],注意事项=row['注意事项'])
            graph.create(node)
        except:
            print("该节点已经存在")
        n=matcher.match("皮肤病",皮肤病名称=row['病名'])
        m=matcher.match("方剂",方剂名称=row['方名'])
        for node in n:
            for node1 in m:
                n_m=Relationship(node,"效验方",node1)
                graph.create(n_m)
        
        
with open("外治方.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        row=eval(row)
        #print(row['病名'])
        #print(row.keys())
        try:
            node=Node("方剂", 方剂名称=row['方名'],功效主治=row['功效'],药材配方=dict2['药材配方'],
                      方剂别名=dict2['方剂别名'],方剂歌诀=dict2['方剂歌诀'],方剂出处=dict2['方剂出处'],
                      方剂组成=row['组成'],药用公用=dict2['药用公用'], 方剂附注=dict2['方剂附注'],
                      方剂制法=row['制法'],方剂鉴别=dict2['方剂鉴别'],趣味记忆=dict2['趣味记忆'],
                      方剂方义=dict2['方剂方义'],各家论述=dict2['各家论述'],加减化裁=dict2['加减化裁'],
                      方剂用法=row['用法'],注意事项=row['注意事项'])
            graph.create(node)
        except:
            print("该节点已经存在")
        n=matcher.match("皮肤病",皮肤病名称=row['病名'])
        m=matcher.match("方剂",方剂名称=row['方名'])
        for node in n:
            for node1 in m:
                n_m=Relationship(node,"外治方",node1)
                graph.create(n_m)    
           
      
with open("其他治法.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        rowDict=row.split(':')
        try:
            node=Node("其他治法", 其他治法名=rowDict[0]+'的其他治法',具体治法=rowDict[1])
            graph.create(node)
        except:
            print("该节点已经存在")
        n=matcher.match("皮肤病",皮肤病名称=rowDict[0])
        m=matcher.match("其他治法",其他治法名=rowDict[0]+'的其他治法')
        for node in n:
            for node1 in m:
                n_m=Relationship(node,"其他治法",node1)
                graph.create(n_m)    
