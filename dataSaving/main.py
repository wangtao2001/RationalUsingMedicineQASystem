# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/05/22, Sat

from dataFormatting import *
from dataToNeo4j import *

neo = DataToNeo4j()  # 连接图数据库
#neo.create_node(node_extraction())  # 创建结点
neo.create_relationship(relationship_extraction())  # 创建关系边
