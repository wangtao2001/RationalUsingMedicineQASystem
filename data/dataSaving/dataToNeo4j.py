# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/05/22, Sat

from py2neo import Node, Relationship, Graph, NodeMatcher


class DataToNeo4j(object):
    def __init__(self, username, password):
        self.graph = Graph('http://localhost:7474/', auth=(username, password))
        print('连接成功')

    def delete_all(self):
        self.graph.delete_all()
        print('已经清空原有数据')

    def create_node(self, node_dict):
        for i in range(5):
            label = list(node_dict.keys())[i]
            for node in node_dict[label]:
                n = Node(label)
                n.update(node)  # 加入属性
                # print(str(n).encode('utf-8').decode('unicode_escape'))
                self.graph.create(n)  # 创建当前结点，标签全为label
        print('结点创建完成')

    def create_relationship(self, relationship_dict):
        matcher = NodeMatcher(self.graph)  # 匹配对象
        for i in range(3):
            a_label = list(relationship_dict.keys())[i]
            for relationship in relationship_dict[a_label]:
                a_id = list(relationship.keys())[0]
                a = matcher.match(a_label).where(_id=a_id).first()  # 起始点
                relationship = relationship[a_id]
                for kv in relationship.items():
                    b_label = kv[0]
                    for b_id in kv[1]:
                        b = matcher.match(b_label).where(_id=b_id).first()  # 终点
                        if b is None:
                            continue  # 有些指向的实体可能并没有存在（未收录）
                        describe = self._get_describe(a_label, b_label)
                        r = Relationship(a, describe, b)
                        # print(str(r))
                        self.graph.create(r)
        print('关系边创建完成')

    @staticmethod
    def _get_describe(a_label, b_label):
        if a_label == 'disease':
            hashmap = {'disease': '并发症', 'medical': '常用治疗药物', 'symptom': '可能症状', 'department': '所属科室', 'check': '需做检查'}
        elif a_label == 'check':
            hashmap = {'disease': '相关疾病', 'symptom': '相关症状', 'department': '所在科室'}
        elif a_label == 'symptom':
            hashmap = {'disease': '可能疾病', 'check': '鉴别检查', 'department': '待就诊科室'}
        return hashmap.get(b_label)



