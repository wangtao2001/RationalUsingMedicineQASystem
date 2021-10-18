# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/09/05, Sun

import re
import pandas as pd
import numpy as np
import random
from py2neo import Graph
import sys


class MyQA(object):
    def __init__(self, question, cypher, answer) -> None:
        super().__init__()
        self.question = question
        self.cypher = cypher
        self.answer = answer

    def get_question(self):
        return self.question

    def get_cypher(self):
        return self.cypher

    def get_answer(self):
        return self.answer

    # def output_str(self) -> str:
    #     return self.question + '\n' + self.cypher + '\n' + self.answer + '\n'

    # def cypher_format(self) -> None:
    #     old_cypher = self.cypher
    #     if '->' in old_cypher:
    #         s = re.search("name:'.*'", old_cypher).group()
    #         name = s[6:-1]
    #         s = re.search("-\[:`.*`]->", old_cypher).group()
    #         rela = s[4:-4]
    #         self.cypher = f"match p=(n)-[r:{rela}]->(m) where n.name='{name}' return m.name"
    #     else:
    #         s = re.search('n:[a-z]+', old_cypher).group()
    #         my_type = s[2:]
    #         s = re.search("name:'.*'", old_cypher).group()
    #         name = s[6:-1]
    #         s = re.search("n\..*", old_cypher).group()
    #         target = s[2:]
    #         self.cypher = f"match (n:{my_type}) where n.name='{name}' return n.{target}"
    #     return self


if __name__ == '__main__':
    path = 'C:\\Users\\Administrator\\Desktop\\标记数据\\9.28-\\'

    # data = pd.read_excel(path+"工作簿1.xlsx", engine="openpyxl", header=None)
    # f = open(path+"3000.txt", 'w')

    # d = {
    #     "match p=(n)-[r:效验方]->(m) where n.皮肤病名称='脱发' return m.方剂名称": '"二至丸" "生发饮" "生发方" "桑麻丸" "神应养真丹" "首乌生发丸" "当归生发汤" "元参方" "生发煎剂" "牧野生发方" "双黑豆" "当归天麻丸" "旱莲草方" "二地方" "全当归方" "当赤斑秃汤" "六味生发饮" "白术泽泻方" "斑秃汤" "普秃方" "治脱一方" "治脱二方" "滋发汤" "常青糖浆" "治脱方" "黄胡生发汤" "首乌三子汤" "二子生发丸" "鬼剃头丸" "妇女脱发方" "补肾生发丸" "首乌黑枣汤" "首乌生发饮" "首乌祛秃汤"',
    #     "match p=(n)-[r:外治方]->(m) where n.皮肤病名称='脱发' return m.方剂名称": '"颠倒散" "冬虫夏草酒" "新补骨脂酊" "生发一方" "生发二方" "生发三方" "百部酒精" "红花生发酊" "柏叶生发酊" "熏洗方" "双黄散" "生发酒" "人参生发酊" "滋发液" "脱发验方" "治秃验方" "生发验方" "侧柏叶方" "鸡蛋油烟" "蛇床治脱方" "生发洗剂"',
    #     "match (n:皮肤病) where n.皮肤病名称 = '脱发' return n.皮肤病病因病理": '"斑秃多因肝肾虚亏，阴血不足，风邪则乘虚而入，风盛血燥，发失所养；此外情志不遂，气血失和也与本病的发生有密切关系。脂溢性脱发多因肝肾亏损，外感风、湿二邪所致。"',
    #     "match p=(n)-[r:病所属证候]->(m) where n.皮肤病名称='脱发' return m.证候名称": '"肝肾不足证" "脾胃湿热证"',
    #     "match (n:皮肤病) where n.皮肤病名称 = '脱发' return n.皮肤病症状特点": '"斑秃：为—种局限性脱发，又名圆秃，本病常表现为头皮突然发生指盖至钱币大圆形脱发区，境界明显。患部除脱发外毫无任何异状，损害边缘头发松动易拔。经过缓慢，可长期静止，亦可迅速发展，病损扩大增多，其至头发全脱成全秃。患合毫无自觉症状，多于无意中发现。病因除去后，头发可完全复原，但可再发。可发于任何年龄。严重者睫毛、眉毛、腋毛、阴毛及全身毫毛均可脱落，称全身脱毛或普秃。脂溢性脱发：是在皮脂溢出的基础上引起的一种脱发，多为年轻的成年男性患者，头皮往往油腻发光，或有大量皮屑，呈灰白色碎小糠秕状，散布于头发中，或头发干燥缺乏光辉，自觉瘙痒。时日长久，前额两侧及头顶部头发开始对称脱落患；患部皮肤光滑发亮。由于毛囊萎缩，常致永久脱发，经过缓慢。"',
    #     "match (n:皮肤病) where n.皮肤病名称 = '脱发' return n.皮肤病定义": '"脱发病(Alopecia)，为常见头皮疾患。原因很多，如内分泌紊乱、营养代谢障碍或神经精神、遗传因素等，也可继发于其它疾病之后，部分病人原因不清。常见脱发有斑秃、脂溢性脱发、早秃、假性斑秃及症状性脱发等数种。"'
    # }

    # keys = list(d.keys())

    # print(data)
    # for i in range(0, 600):
    #     loc = data.iloc[i]
    #     f.write(loc[0].strip()+'\n')
    #     if loc[1] in keys:
    #         f.write(loc[1].strip()+'\n')
    #         f.write(d[loc[1]]+'\n')
    #         if loc[1] == "match p=(n)-[r:效验方]->(m) where n.皮肤病名称='脱发' return m.方剂名称":
    #             f.write(
    #                 "match p=(n)-[r:外治方]->(m) where n.皮肤病名称='脱发' return m.方剂名称"+'\n')
    #             f.write(
    #                 d["match p=(n)-[r:外治方]->(m) where n.皮肤病名称='脱发' return m.方剂名称"]+'\n')
    #     else:
    #         print(i)
    #     f.write("\n")

    # data = pd.read_excel(path+"5001-7000.xlsx", engine="openpyxl", header=None)
    # f = open(path+"5001-7000.txt", 'w', encoding='utf-8')

    # my_list = []

    # for i in range(120):
    #     loc = data.iloc[i]
    #     my_list.append(MyQA(loc[0], loc[1], loc[2]))

    # for i in my_list:
    #     f.write(i.get_question()+'\n')
    #     f.write(i.get_cypher()+'\n')
    #     f.write(i.get_answer()+'\n')
    #     f.write('\n')

    # f.close()
    driver = Graph('http://localhost:7474/', auth=('neo4j', 'qazplm-55454'))

    # zhenghou_list = []
    # find = driver.run('match (n:证候) return n.证候名称')
    # for i in find:
    #     zhenghou_list.append(str(i).strip("'"))

    # fangji_list = []
    # find = driver.run('match (n:方剂) return n.方剂名称')
    # for i in find:
    #     fangji_list.append(str(i).strip("'"))

    # zhongyao_list = []
    # find = driver.run('match (n:中药) return n.中药名称')
    # for i in find:
    #     zhongyao_list.append(str(i).strip("'"))

    # data = {
    #     'match p=(n)-[:所属证候]->(m) where m.证候名称="{}" return n.方剂名称': ([
    #         '{}需要吃什么中药',
    #         '{}用什么中药治疗',
    #         '什么方子可以治疗{}',
    #         '有{}怎么治疗',
    #         '{}能怎么治疗',
    #         '{}能吃什么中药',
    #         '{}用什么方治疗比较好',
    #         '{}要吃什么药',
    #         '{}吃什么药比较好',
    #         '{}用什么方剂治疗'
    #     ], zhenghou_list),
    #     'match p=(n)-[:所属证候分类]->(m) where n.证候名称="{}" return m.证候分类名称': ([
    #         '{}是什么类型的',
    #         '{}属于什么分类',
    #         '{}该分什么类',
    #         '{}是属于什么类型的',
    #         '{}归属到什么类型的证候中去',
    #         '{}是什么类型的证候',
    #         '{}是什么类型的证'
    #     ], zhenghou_list),
    #     'match p=(n)-[:入药方剂]->(m) where m.方剂名称="{}" return n.中药名称': ([
    #         '{}需要用什么中药入药',
    #         '{}是哪些中药组成的',
    #         '{}是哪些药材组成的',
    #         '{}需要用到些什么中药',
    #         '哪些中药组成了{}',
    #         '{}可能用到了些什么中药',
    #         '{}用到了哪些药'
    #     ], fangji_list),
    #     'match p=(n)-[:属于]->(m) where n.中药名称="{}" return m.中药分类名称': ([
    #         '{}属于什么分类',
    #         '{}属于什么药',
    #         '{}该归属到什么药',
    #         '{}是什么类型的'
    #     ], zhongyao_list),
    #     'match p=(n)-[:所属辨证法]->(m) where n.证候名称="{}" return m.辨证法名称': ([
    #         '{}是怎样来判断的',
    #         '{}用什么辩证法来判断',
    #         '{}的判断属于什么辩证法'
    #     ], zhenghou_list),
    #     'match p=(n)-[:反]->(m) where n.中药名称="{}" return m.中药名称': ([
    #         '{}有哪些反药',
    #         '{}与哪些药相反',
    #         '{}与哪些药不能一起使用',
    #         '{}与哪些药不能一起用'
    #     ], zhongyao_list),
    #     'match p=(n)-[:畏]->(m) where n.中药名称="{}" return m.中药名称': ([
    #         '{}有哪些畏药',
    #         '{}与哪些药向畏',
    #         '{}与什么药不建议一起使用',
    #         '{}与什么药不建议一起用'
    #     ], zhongyao_list)
    # }

    # qa_list = []
    # all_node = set()

    # while True:
    #     index = random.randint(0, 6)
    #     cypher = list(data.keys())[index]

    #     node_list = data[cypher][1]
    #     index = random.randint(0, len(node_list)-1)
    #     node = node_list[index]

    #     question_list = data[cypher][0]
    #     index = random.randint(0, len(question_list)-1)
    #     question = question_list[index].format(node)
    #     cypher = cypher.format(node)

    #     answer = []
    #     find = driver.run(cypher=cypher)
    #     for i in find:
    #         answer.append('"'+str(i).strip("'")+'"')
    #     if len(answer) == 0 or answer[0] == '"None"':
    #         continue
    #     else:
    #         answer = ' '.join(answer)
    #         all_node.add(node)

    #         qa_list.append(
    #             MyQA(question=question, cypher=cypher, answer=answer))

    #         if len(qa_list) == 250:
    #             break

    # f = open(path+"9001-10500.txt", 'w', encoding='utf-8')
    # f_node = open(path+"9001-10500提及.txt", 'w', encoding='utf-8')

    # for i in qa_list:
    #     f.write(i.get_question()+'\n')
    #     f.write(i.get_cypher()+'\n')
    #     f.write(i.get_answer()+'\n')
    #     f.write('\n')

    # for node in all_node:
    #     f_node.write(node+'\t'+node)
    #     f_node.write('\n')

    # f.close()
    # f_node.close()

    # 1. 问句模板+查询模板
    # 2. 纳入所有实体
    # 3. 随机匹配实体 + 问句 , 输出

    disease = []
    find = driver.run('match (n:disease) return n.name')
    for i in find:
        disease.append(str(i).strip("'"))

    # medical = []
    # find = driver.run('match (n:medical) return n.name')
    # for i in find:
    #     medical.append(str(i).strip("'"))

    # symptom = []
    # find = driver.run('match (n:symptom) return n.name')
    # for i in find:
    #     symptom.append(str(i).strip("'"))

    # check = []
    # find = driver.run('match (n:check) return n.name')
    # for i in find:
    #     check.append(str(i).strip("'"))

    data = {
        'match p=(n)-[:并发症]->(m) where n.name="{}" return m.cure_rate': ([
            '{}引起的并发症治愈率有多高',
            '{}引起的并发症的治愈率都有多高',
            '{}能够导致治愈率都为为多高的并发症',
            '患有{}，并发症的治愈率都有多高',
            '{}可能的并发症的治愈率都是多少',
            '{}能够引起的并发症的治愈率都很低吗'],
            disease),
        'match p=(n)-[:需做检查]->(m) where n.name="{}" return m.atten': ([
            '做{}相关检查的时候都要注意些什么',
            '做{}相关检查时有什么需要注意的',
            '患有{}，做检查的时候要注意些什么',
            '得了{}，做检查的时候有什么要注意的吗',
            '有{}，需要做的检查都要注意些什么',
            '与{}相关的检查有什么注意事项'],
            disease),
        'match p=(n)-[:可能症状]->(m) where n.name="{}" return m.cause': ([
            '得了{}，这些症状都是怎么引起的',
            '患有{}有关的症状，可能都是什么原因导致的',
            '{}相关的症状，都是什么导致的',
            '{}相关的症状，可能都是什么引起的',
            '可能都是什么引起{}有关的症状的',
            '什么情况下会导致{}有关的症状',
            '什么会导致{}相关的症状'],
            disease),
        'match p=(n)-[:常用治疗药物]->(m) where n.name="{}" return m.function': ([
            '能够治疗{}等疾病的药物的功能主治都什么些什么',
            '治疗{}等疾病的药物的都有哪些功能主治',
            '患有{},使用的药物的功能主治都是什么',
            '治{}的药物都能治疗什么疾病',
            '{}常用的治疗药物的功能主治都有什么'],
            disease)
    }

    qa_list = []
    all_node = set()

    while True:
        index = random.randint(0, len(data)-1)
        cypher = list(data.keys())[index]

        node_list = data[cypher][1]
        index = random.randint(0, len(node_list)-1)
        node = node_list[index]

        question_list = data[cypher][0]
        index = random.randint(0, len(question_list)-1)
        question = question_list[index].format(node)
        cypher = cypher.format(node)

        answer = []
        find = driver.run(cypher=cypher)
        for i in find:
            answer.append('"'+str(i).strip("'")+'"')
        if len(answer) == 0 or answer[0] == '"None"':
            continue
        else:
            answer = ' '.join(answer)
            all_node.add(node)

            qa_list.append(
                MyQA(question=question, cypher=cypher, answer=answer))

            if len(qa_list) == 150:
                break

    f = open(path+"问答（两跳）.txt", 'w', encoding='utf-8')
    f_node = open(path+"提及.txt", 'w', encoding='utf-8')

    for i in qa_list:
        f.write(i.get_question()+'\n')
        f.write(i.get_cypher()+'\n')
        f.write(i.get_answer()+'\n')
        f.write('\n')

    for node in all_node:
        f_node.write(node+'\t'+node)
        f_node.write('\n')

    f.close()
    f_node.close()
