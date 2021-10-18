# -*- coding:utf-8 -*-


from py2neo import Graph,Node,Relationship,NodeMatch
from py2neo.matching import *
class MedicalGraph:
    def __init__(self):
        self.graph = Graph('http://localhost:7474',username='neo4j',password='houyijia123456')

    def inputyaocai(self):
        # 共7类节点
        yaocais = [] #药材
        bieming = []


        for i in open(r"药物名称.txt", 'r', encoding='utf-8') :
            if '(' in i:
                i = str.replace(i, '(', '#', 1)
                i = i[:-3]
                name = i.split('#')
                yaocais.append(name[0])
                bieming.append(name[1])
            else:
                yaocais.append(i[:-1])
                bieming.append("null")


        xingweis = []  # 性味
        guijings = []  # 归经
        yaocaixinxis = []  # 药材信息
        rels_yaocai_xingwei = []
        rels_yaocai_guijing = []
        count = 0
        for line in open(r"完整属性.txt", 'r', encoding='utf-8') :
            yaocai_dict = eval(line)
            yaocai_name = yaocais[count]
            yaocai_dict["【名称】"] = yaocai_name
            count += 1

            if yaocai_dict['【性味】'] != "null":
                xingwei = yaocai_dict['【性味】']
                xingwei = str.replace(xingwei ,'《' , '')
                xingwei = str.replace(xingwei, '》' , '')
                xingwei = str.replace(xingwei, '\'' , '')
                xingwei = str.replace(xingwei, '\"' , '')
                xingweis.append(xingwei)
                rels_yaocai_xingwei.append([yaocai_name,xingwei])

            if yaocai_dict['【归经】'] != "null":
                guijing = yaocai_dict['【归经】']
                guijing = str.replace(guijing ,'《' , '')
                guijing = str.replace(guijing , '》', '')
                guijing = str.replace(guijing , '\'', '')
                guijing = str.replace(guijing , '\"', '')
                guijings.append(guijing)
                rels_yaocai_guijing.append([yaocai_name,guijing])

            yaocaixinxis.append(yaocai_dict)
        return  set(yaocais), set(xingweis), set(guijings), yaocaixinxis, rels_yaocai_xingwei,rels_yaocai_guijing

    def inputfangji(self):
        fangjis = []

        for i in open(r"入药方剂名.txt",'r', encoding='utf-8'):
            fangjis = []
            for i in open("入药方剂名.txt", "r", encoding="utf-8"):
                if ':' in i:
                    continue
                elif '的入药方剂' in i:
                    continue
                else:
                    i = i.replace('\n', '')
                    fangjis.append(i)
        fangjifenleis = []  # 方剂分类
        fangji_infos = []  # 入药方剂信息
        rels_yaocai_fangji = []
        rels_fangjiclassify = []
        count = 0
        for line in open(r"入药方剂.txt", 'r', encoding='utf-8') :
            fangji_dict = eval(line)
            count += 1
            fangji_name = fangjis[count - 1]
            fangji_dict["名称"] = fangji_name

            if  fangji_dict["所属分类："] != "null":
                fangjifenlei = fangji_dict['所属分类：']
                fangjifenleis.append(fangjifenlei)
                rels_fangjiclassify.append([fangjifenlei, fangji_name])

            if  fangji_dict['药材配方：'] != "null":
                yaocainame = fangji_dict['药材配方：'].split(",")
                for i in yaocainame:
                    rels_yaocai_fangji.append([i, fangji_name])

            fangji_infos.append(fangji_dict)
        return set(fangjis), set(fangjifenleis),fangji_infos,rels_fangjiclassify, rels_yaocai_fangji


    #建立节点
    def create_node(self,label, nodes):
        count = 0
        for node_name in nodes:
            node = Node(label, name=node_name)
            self.graph.create(node)
            count += 1
            print(count, len(nodes))
        return

    def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
        count = 0
        # 去重处理
        all = len(edges)
        for edge in edges:
            p = edge[0]
            q = edge[1]
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" % (start_node, end_node, p, q, rel_type, rel_name)
            try:
                self.graph.run(query)
                count += 1
                print(rel_type, count, all)
            except Exception as e:
                print(e)
        return

       # 创建节点
    def create_yaocainodes(self):
        YaoCai, XingWei, GuiJing, yaocaixinxis, rels_yaocai_xingwei, rels_yaocai_guijing = self.inputyaocai()
        for yaocai_dict in yaocaixinxis:
            node = Node("YaoCai", name=yaocai_dict['【名称】'], pinyin_name=yaocai_dict['【汉语拼音】'],
                        composition=yaocai_dict['【成份】'],effect=yaocai_dict['【功能主治】'], usage=yaocai_dict['【用法用量】'],
                        morphology=yaocai_dict['【植物形态】'], part=yaocai_dict['【药用部位】'],source=yaocai_dict['【来自何书】'],
                        en_name=yaocai_dict['【名称英】'], jianbie=yaocai_dict['【药材鉴别】'], yaoli=yaocai_dict['【药理作用】'],
                        paozhi=yaocai_dict['【炮制】'], yiji=yaocai_dict['【宜忌】'],zhucang=yaocai_dict['【贮藏】'],
                        side_effect=yaocai_dict['【副作用】'],apply=yaocai_dict['【临床应用】'], other_name=yaocai_dict['【别名】'])
            self.graph.create(node)
        self.create_node('GuiJing', GuiJing)
        self.create_node('XingWei', XingWei)
        return

    def create_fangjinodes(self):
        FangJi, FangJiFenLei, fangji_infos, rels_fangjiclassify, rels_yaocai_fangji = self.inputfangji()

        for fangji_dict in fangji_infos:
            node = Node("FangJi", name=fangji_dict['名称'], yaoyonggongyong=fangji_dict['药用公用：'],gongxiaozhuzhi=fangji_dict["功效主治："], zucheng=fangji_dict["组成："],fangjichuchu=fangji_dict["方剂出处："], yaocaipeifang=fangji_dict["药材配方："], angjiyongfa=fangji_dict["方剂用法："], fangjifuzhu=fangji_dict["方剂附注："])
            self.graph.create(node)

        self.create_node('FangJiFenLei', FangJiFenLei)
        return


    def create_yaocairels(self):
        YaoCai, XingWei, GuiJing, yaocai_infos, rels_yaocai_xingwei, rels_yaocai_guijing = self.inputyaocai()

        self.create_relationship("YaoCai", "GuiJing", rels_yaocai_guijing, 'yaocai_guijing', '归经')
        self.create_relationship('YaoCai', 'XingWei', rels_yaocai_xingwei, 'yaocai_xingwei ', '性味')

    def create_fangjirels(self):
        FangJi, FangJiFenLei, fangji_infos, rels_fangjiclassify, rels_yaocai_fangji = self.inputfangji()

        self.create_relationship('YaoCai', 'FangJi', rels_yaocai_fangji, 'yaocai_fangji', '方剂组成')
        self.create_relationship('FangJiFenLei', 'FangJi', rels_fangjiclassify, 'fangjiclassify', '所属分类')


if __name__ == '__main__':
    handler = MedicalGraph()

    handler.create_yaocainodes()
    handler.create_yaocairels()

    handler.create_fangjinodes()
    handler.create_fangjirels()





