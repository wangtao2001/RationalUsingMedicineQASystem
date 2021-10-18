# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/10/07, Thurs

# 方剂分类新增4个实体:润泽皮肤方、驻颜祛皱方、洁面增白方、香身美体方,新增一个描述属性 (:方剂分类 {方剂分类名称, 方剂分类描述})
# 方剂新增 159个实体 <使用美容方剂代替原方剂，因为原来的方剂有约束，两类方剂可能同名导致不能导入>
# 方剂指向方剂分类关系新增一个分类类型属性 (:方剂)-[:所属分类 {分类类型}]->(:方剂分类) 即内治方、外治方
# 方剂指向中药关关系新增两个属性 (:方剂)-[:入药方剂 {用量, 治法}]->(:中药) 775条

import re
from py2neo import Graph, Node, Relationship, NodeMatcher
import json
from py2neo import errors

user = 'neo4j'
pwd = 'qazplm-55454'
driver = Graph('http://localhost:7474/', auth=(user, pwd))
matcher = NodeMatcher(driver)

with open('./data.json', 'r', encoding='utf8') as fp:
    data = json.load(fp)


def dataToNeo4j():
    def create_node(f):
        n = Node("美容方剂", 方剂名=f["方剂名"], 来源=f["来源"], 功效=f["功效"],
                 制法=f["制法"], 用法=f["用法"], 备注=f["备注"])
        return n

    s = Node('美容方', 名称='美容方')
    driver.create(s)
    for i in range(4):
        item = data[i]  # 方剂分类
        a = Node("方剂分类", 方剂分类名称=item["方剂分类名称"], 方剂分类描述=item["方剂分类描述"])
        driver.create(a)
        driver.create(Relationship(a, "所属", s))
        for f in item["内治方"]:
            b = create_node(f)
            driver.create(b)
            driver.create(Relationship(a, "内治方", b))
        for f in item["外治方"]:
            c = create_node(f)
            driver.create(c)
            driver.create(Relationship(a, "外治方", c))

    dlist = list(matcher.match("中药"))  # node list

    def create_rela(f):
        a = matcher.match("美容方剂", 方剂名=f["方剂名"]).first()
        for dr in list(f["组成"].keys()):
            try:
                pattern = re.compile('\(.*\)')
                fun = pattern.search(dr).group()
                fun = fun[1:-1]
            except AttributeError:
                fun = ""
            dosage = f["组成"][dr]
            dr = dr.replace(fun, "")
            for d in dlist:
                if d["中药名称"] == dr:
                    driver.create(Relationship(
                        d, "入药方剂", a, 用量=dosage, 制法=fun))
                    break
            else:
                pass

    for i in range(4):
        item = data[i]  # 方剂分类
        for f in item["内治方"]:
            create_rela(f)
        for f in item["外治方"]:
            create_rela(f)


def delete_all():
    def func(f):
        driver.run(
            f"match(n:方剂) where n.方剂名 = '{f['方剂名']}' detach delete n")

    driver.run(f"match(n:美容方) detach delete n")
    for i in range(4):
        item = data[i]  # 方剂分类
        driver.run(
            f"match(n:方剂分类) where n.方剂分类名称 = '{item['方剂分类名称']}' detach delete n")
        for f in item["内治方"]:
            func(f)
        for f in item["外治方"]:
            func(f)


if __name__ == "__main__":
    delete_all()
    dataToNeo4j()
