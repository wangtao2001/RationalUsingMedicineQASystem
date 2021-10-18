# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:11:04 2021

@author: 独顽似鄙
"""
from py2neo import Graph,Node,Relationship,NodeMatcher
from py2neo.matching import *

username = 'neo4j'
password = 'qazplm-55454'
g = Graph('http://localhost:7474/', auth=(username, password))

def create_relationship(start_node, end_node, edges, rel_type, rel_name):
    set_edges = []
    for edge in edges:
        set_edges.append('###'.join(edge))
        
    for edge in set(set_edges):
        edge = edge.split('###')
        p = edge[0]
        q = edge[1]
        
        k = "match(p:%s),(q:%s) where p."+start_node+"名称"+"='%s'and q."+end_node+"名称"+"='%s' create (p)-[rel:%s{name:'%s'}]->(q)"
        query = k % (start_node, end_node, p, q, rel_type, rel_name)
        try:
            g.run(query)
        except Exception as e:
            print(e)
    return

with open("医药查询平台\\方-药.txt","r",encoding = "utf-8") as f:
    rels_yaocai_fangji= [eval(dict) for dict in f.readlines()]
    
create_relationship('中药', '方剂', rels_yaocai_fangji, '入药方剂', '入药方剂')