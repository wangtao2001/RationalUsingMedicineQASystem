# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 09:44:24 2021

@author: 独顽似鄙
"""

from py2neo import Graph,Node,Relationship,NodeMatcher
from py2neo.matching import *



username = 'neo4j'
password = 'qazplm-55454'
g = Graph('http://localhost:7474/', auth=(username, password))

def create_relationship(start_node, end_node, edges, rel_type, rel_name):
    # 去重处理
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


def get_data():
    
    zheng_info = []
    rel_zhengs = []
    rel_bianzheng = []
    
    for line in open("证\\证候.txt","r",encoding = "utf-8"):
        if line == '\n':
            continue
        zheng_info.append(eval(line))
        zhengdict = eval(line)
        rel_zhengs.append([zhengdict['证名'],zhengdict['所属证候分类']])
        rel_bianzheng.append([zhengdict['证名'],zhengdict['辨证法']])
    
    hou_info = []
    
    for i in open("证\\证候大类.txt","r",encoding = "utf-8"):
        if i == '\n':
            continue
        hou_info.append(eval(i))
        houdict = eval(i)
        rel_bianzheng.append([houdict['辨证法'],houdict['证名']])
    
    bianzheng_info = []
    for j in open('证\\辨证法分类.csv','r',encoding = "ansi"):
       if j == '\n':
           continue
       dict = j.split(',',1)
       bianzheng_info.append({'辨证法':dict[0],'含义':dict[1]})
    
    return zheng_info,rel_zhengs,rel_bianzheng,hou_info,bianzheng_info

def create_zhengnode():
    zheng,rel_zhengs,rel_bianzheng,hou,bianzheng = get_data()
    
    for zheng_dict in zheng:
        try:
            node = Node('证候',证候名称=zheng_dict['证名'],证候英文名=zheng_dict['英文名称'],\
                        证候别名=zheng_dict['别名'],证候病机=zheng_dict['病机'],\
                        临床表现=zheng_dict['临床表现'])
            g.create(node)
        except Exception as e:
            print(e)
    
    for hou_dict in hou:
        try:
            node = Node('证候分类',证候分类名称=hou_dict['证名'],证候分类英文名=hou_dict['英文名称'],\
                        证候分类别名=hou_dict['别名'],证候分类含义=hou_dict['含义'],\
                        证候分类附注=hou_dict['注'])
            g.create(node)
        except Exception as e:
            print(e)
    
    for bianzheng_dict in bianzheng:
        try:
            node = Node('辨证法',辨证法名称=bianzheng_dict['辨证法'],辨证法含义=bianzheng_dict['含义'])
            g.create(node)
        except Exception as e:
            print(e)
    
    
    create_relationship('证候','证候分类', rel_zhengs,'所属证候分类', '所属证候分类')
    create_relationship('证候','证候', rel_zhengs,'所属证候分类', '所属证候分类')
    create_relationship('证候分类','证候分类', rel_zhengs,'所属证候分类', '所属证候分类')
    
    create_relationship('证候分类','辨证法', rel_bianzheng,'所属辨证法', '所属辨证法')
    create_relationship('证候','辨证法', rel_bianzheng,'所属辨证法', '所属辨证法')         

def create_zhengfang():
    
    rel_zhengfangs = []
    
    for line in open("证\\证-方剂.csv","r",encoding = "ansi"):
        if line == '\n':
            continue
        dict = line.split(',',1)
       
        rel_zhengfangs.append([dict[1][:-1],dict[0]])
        
    
    
    for line in open("证\\0-500.csv",'r',encoding = 'ansi'):
        if line == '\n':
            continue
        dict = line.split(',',1)
        fang = dict[1][:-1].split('，')
        for i in fang:
            rel_zhengfangs.append([i,dict[0]])
    
    create_relationship('方剂','证候',rel_zhengfangs,'所属证候', '所属证候')

    return 

if __name__ == '__main__':
    create_zhengnode()
    print("证候节点创建完毕")
    create_zhengfang()
    print("证候-方剂关系创建完毕")
    