# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/05/22, Sat

from py2neo import Node, Relationship, Graph, NodeMatcher

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
        matcher = NodeMatcher(self.graph)  # 匹配对象
        for i in range(5):
            a_label = list(relationship_dict.keys())[i]
            for relationship in relationship_dict[label]:
                a_id = list(relationship.keys())[0]
                a = matcher.match(a_label).where(id=a_id)  # 起始点
                relationship = relationship["id"]
                for kv in relationship.items():
                    b_label = kv[0]
                    for b_id in kv[1]:
                        b = matcher.match(b_label).where(id=b_id)  # 终点
                        describe = self._get_describe(a_label, b_label)
                        this = Relationship(a, describe, b)
                        self.graph.create(this)

    @staticmethod
    def _get_describe(a_label, b_label):
        if a_label == 'disease':
            if b_label == 'disease':
                return '并发症'
            if b_label == 'medical':
                return '常用药品'
            if b_label == 'symptom':
                return '可能症状'
            if b_label == 'check':
                return '需做检查'
            if b_label == 'department':
                return '需要挂号科室'
        if a_label == 'check':
            if b_label == 'disease':
                return '相关疾病'
            if b_label == 'symptom':
                return '相关症状'
            if b_label == 'department':
                return '所在科室'
        if a_label == 'symptom':
            if b_label == 'disease':
                return '可能疾病'
            if b_label == 'check':
                return '鉴别检查'
            if b_label == 'department':
                return '待就诊科室'



