# -*- coding:utf-8 -*-
#导入
from py2neo import Graph,Node,Relationship,NodeMatch
from py2neo.matching import *

graph = Graph('http://localhost:7474',username='neo4j',password='houyijia123456')
a=Node('分类',lable="中药分类",name="开窍药")
graph.create(a)
'''b=Node('分类',lable="中药分类",name="理气药")
graph.create(b)
c=Node('分类',lable="中药分类",name="平喘药")
graph.create(c)
d=Node('分类',lable="中药分类",name="平肝息风药")
graph.create(d)
e=Node('分类',lable="中药分类",name="温里药")
graph.create(e)
f=Node('分类',lable="中药分类",name="泻下药")
graph.create(f)
g=Node('分类',lable="中药分类",name="涌吐药")
graph.create(g)
h=Node('分类',lable="中药分类",name="止血药")
graph.create(h)'''
count=0
matcher=NodeMatch(graph)

for i in range(320,338):
 print (1)
 n1=matcher.match('',id=)
 for node1 in
