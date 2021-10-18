# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:12:45 2021

@author: 宋小兰
"""


from py2neo import Graph,Node,Relationship,NodeMatch
graph=Graph(host='localhost',auth=('neo4j','neo4j'))
    
mingcheng=[]
count=2062
with open("清热药药名_name.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        mingcheng.append(row)
for i in mingcheng:
    count=count+1
    node=Node("中药", name=i,id=count)
    graph.create(node)

    
        
                
                
