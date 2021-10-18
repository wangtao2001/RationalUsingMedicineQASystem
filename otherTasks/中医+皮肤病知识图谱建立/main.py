# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:28:37 2021

@author: 独顽似鄙
"""

import os
from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','qazplm-55454'))


graph.schema.create_uniqueness_constraint('中药', '中药名称')
graph.schema.create_uniqueness_constraint('方剂', '方剂名称')
graph.schema.create_uniqueness_constraint('中药分类', '中药分类名称')
graph.schema.create_uniqueness_constraint('方剂分类', '方剂分类名称')
graph.schema.create_uniqueness_constraint('证候', '证候名称')
graph.schema.create_uniqueness_constraint('证候分类', '证候分类名称')
graph.schema.create_uniqueness_constraint('辨证法', '辩证法名称')
graph.schema.create_uniqueness_constraint('皮肤病', '皮肤病名称')
graph.schema.create_uniqueness_constraint('其他治法', '其他治法名称')

with open('医药查询平台\\中药.py',encoding='utf-8') as f:
    exec(f.read())
print('1')

with open('医药查询平台\\方剂.py',encoding='utf-8') as f:
    exec(f.read())
print('2')

with open('医药查询平台\\方剂-方剂分类.py',encoding='utf-8') as f:
    exec(f.read())
print('3')

with open('39健康网1\\药+方.py',encoding='utf-8') as f:
    exec(f.read())
print('4')

with open('39健康网2\\39健康网.py',encoding='utf-8') as f:
    exec(f.read())
print('5')

with open('39健康网1\\方.py',encoding='utf-8') as f:
    exec(f.read())
print('6')

with open('医药查询平台\\方-药.py',encoding='utf-8') as f:
    exec(f.read())
print('7') 

with open('证\\知识图谱-证+证-方.py',encoding='utf-8') as f:
    exec(f.read())
print('8')

with open('皮肤病\\皮肤病.py',encoding='utf-8') as f:
    exec(f.read())
print('9')

for i in ['入药方剂','属于','所属分类','所属证候','所属证候分类','所属辨证法','反','畏','其他治法','外治方','效验方','病所属证候']:
    query = "MATCH (a)-[r:`"+i+"`]->(b) WITH a, b, TAIL (COLLECT (r)) as rr WHERE size(rr)>0 FOREACH (r IN rr | DELETE r)"
    graph.run(query)
