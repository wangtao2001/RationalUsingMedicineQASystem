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
        dosage = str(f['组成'])[1:-1].replace("'", "")
        n = Node("美容方剂", 方剂名=f["方剂名"], 来源=f["来源"], 功效=f["功效"],
                 治法=f["治法"], 用法=f["用法"], 备注=f["备注"], 配伍用量=dosage)
        return n

    for i in range(4):
        item = data[i]  # 方剂分类
        a = Node("方剂分类", 方剂分类名称=item["方剂分类名称"], 方剂分类描述=item["方剂分类描述"])
        driver.create(a)
        for f in item["内治方"]:
            b = create_node(f)
            driver.create(b)
            driver.create(Relationship(a, "所属分类", b, 分类类型="内治方"))
        for f in item["外治方"]:
            c = create_node(f)
            driver.create(c)
            driver.create(Relationship(c, "所属分类", a, 分类类型="外治方"))

    dlist = list(matcher.match("中药"))  # node list

    def create_rela(f):
        a = matcher.match("美容方剂", 方剂名=f["方剂名"]).first()
        for dr in list(f["组成"].keys()):
            try:  # 去掉括弧
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
            else:  # 没有匹配，创建中药节点
                d = Node("中药", 中药名称=dr)
                try:
                    driver.create(d)
                    driver.create(Relationship(
                        d, "入药方剂", a, 用量=dosage, 制法=fun))
                except:
                    pass

    for i in range(4):
        item = data[i]  # 方剂分类
        for f in item["内治方"]:
            create_rela(f)
        for f in item["外治方"]:
            create_rela(f)

    print("导入成功")


def delete_all():
    def func(f):
        driver.run(
            f"match(n:美容方剂) where n.方剂名 = '{f['方剂名']}' detach delete n")

    for i in range(4):
        item = data[i]  # 方剂分类
        driver.run(
            f"match(n:方剂分类) where n.方剂分类名称 = '{item['方剂分类名称']}' detach delete n")
        for f in item["内治方"]:
            func(f)
        for f in item["外治方"]:
            func(f)

    print("删除成功")


if __name__ == "__main__":
    delete_all()
    dataToNeo4j()
