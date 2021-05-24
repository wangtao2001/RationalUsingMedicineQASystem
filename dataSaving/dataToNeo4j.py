# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/05/22, Sat

from py2neo import Node, Relationship, Graph

username = 'neo4j'
password = 'qazplm-55454'


class DataToNeo4j(object):
    def __init__(self):
        # 建立连接
        self.graph = Graph('http://localhost:7474/', auth=(username, password))
        # 清空数据库
        self.graph.delete_all()

    def create_node(self, node_dict):
        for i in range(5):
            label = list(node_dict.keys())[i]
            for node in node_dict[label]:
                this = Node(label)
                this.update(node)  # 加入属性
                self.graph.create(this)  # 创建当前结点，标签全为label

    def create_relationship(self, relationship_dict):
        pass
