# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:07:16 2021
创建部分39健康网的中药节点，
中药与中药分类之间的关系，
中药与方剂之间的关系，
方剂与方剂分类之间的关系
"""
from py2neo import Graph,Node,Relationship,NodeMatcher
from py2neo.matching import *

class buildzhongyaodb:
    def __init__(self,path,fenlei):
        self.path = path
        self.fenlei = fenlei
        username = 'neo4j'
        password = 'qazplm-55454'
        self.g = Graph('http://localhost:7474/', auth=(username, password))
        
    def delete_all(self):
      self.g.delete_all()
    
    def inputfangji(self):
        fangjis = []
        for i in  open(path+"\\"+fenlei+"\\"+"入药方剂名.txt","r",encoding = "utf-8"):
            if '：' in i:
                continue
            elif '的入药方剂' in i:
                continue
            elif i == '\n':
                continue
            else:
                i = i.replace('\n','')
                fangjis.append(i)
        
        fangji_infos = []
        fangjifenleis = []
        rels_fangjiclassify = []
        rels_yaocai_fangji = []
        cnt = 0
        
        for line in  open(path+"\\"+fenlei+"\\"+"入药方剂完整属性.txt","r",encoding = "utf-8"):
            if line == '\n':
                continue
           
            fangji_dict = eval(line)
            cnt += 1
            fangji_name = fangjis[cnt-1]
            fangji_dict["名称"] = fangji_name

            if fangji_dict['所属分类：'] != "null":
               fangjifenlei = fangji_dict['所属分类：']
               fangjifenleis.append(fangjifenlei)
               rels_fangjiclassify.append([ fangji_name,fangjifenlei])
            
            if fangji_dict['药材配方：'] != "null":
                yaocainame = fangji_dict['药材配方：'].split(",")
                for i in yaocainame:
                    rels_yaocai_fangji.append([i,fangji_name])
       
            fangji_infos.append(fangji_dict)
        return set(fangjis),set(fangjifenleis),fangji_infos,rels_fangjiclassify,rels_yaocai_fangji
    
    def inputyaocai(self):
        yaocais = []
        rels_yaocai_fenlei = []
        for i in  open(path+"\\"+fenlei+"\\"+"药物名称.txt","r",encoding = "utf-8"):
            if '(' in i:
                i = str.replace(i,'(','#',1)
                i = i[:-3]
                name = i.split('#')
                yaocai_name = name[0]
        
            elif i == '\n':
                continue
            else:
                yaocai_name = i[:-1]
                
            yaocais.append(yaocai_name)
            rels_yaocai_fenlei.append([yaocai_name,fenlei])
        
        yaocai_infos = []
        count = 0
        for line in  open(path+"\\"+fenlei+"\\"+"完整属性.txt","r",encoding = "utf-8"):
            if line == '\n':
                continue
            yaocai_dict = eval(line)
            yaocai_name = yaocais[count]
            yaocai_dict["【名称】"] = yaocai_name
            count += 1
            
            yaocai_infos.append(yaocai_dict)
            
        
            
        return set(yaocais),yaocai_infos,rels_yaocai_fenlei
    
               
    def create_node(self,label,nodes):
        count = 0
        for node_name in nodes:
            try:
                node = Node(label, 方剂分类名称=node_name)
                self.g.create(node)
                count += 1
                #print(count, len(nodes))
            except Exception as e:
                print(e)
        return
    
    def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
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
                self.g.run(query)
            except Exception as e:
                print(e)
        return
    
    
    #创建药材有关节点
    def create_yaocai(self):
        YaoCai,yaocai_infos,rels_yaocai_fenlei = self.inputyaocai()
       
        for yaocai_dict in yaocai_infos:
            try:
                node = Node("中药", 中药名称=yaocai_dict['【名称】'],中药拼音=yaocai_dict['【汉语拼音】'],\
                            加工采集=yaocai_dict['【加工采集】'],化学成分=yaocai_dict['【成份】'],\
                            功能主治=yaocai_dict['【功能主治】'],用法用量=yaocai_dict['【用法用量】'],\
                            形态特征=yaocai_dict['【植物形态】'],药用部位=yaocai_dict['【药用部位】'],\
                            中药出处=yaocai_dict['【来自何书】'],中药英文名=yaocai_dict['【名称英】'],\
                            中药鉴别=yaocai_dict['【药材鉴别】'],药理作用=yaocai_dict['【药理作用】'],\
                            炮制方法=yaocai_dict['【炮制】'],中药宜忌=yaocai_dict['【宜忌】'],\
                            保存方法=yaocai_dict['【贮藏】'],副作用=yaocai_dict['【副作用】'],\
                            临床应用=yaocai_dict['【临床应用】'],中药别名=yaocai_dict['【别名】'],\
                            性味归经=yaocai_dict['【性味】']+yaocai_dict['【归经】'],毒理作用='null',\
                            饮片性状='null',常见伪品='null',药膳食疗='null',\
                            药材性状='null',饮片名称='null',相关配伍='null',鉴别用药='null',\
                            注意事项='null',分布区域='null',医保类型='null',植物信息='null',中药附注='null',\
                            道地产区='null',中药种属='null',生长环境='null',\
                            繁殖方式='null',成份检验='null',\
                            药品检验='null',中药简介='null',中药拉丁名='null',\
                            中药毒性='null',现代研究='null') 
                   
                self.g.create(node)
               
                
            except Exception as e:
                print(e)
        
        try:
            node = Node("中药分类", 中药分类名称=self.fenlei)
            self.g.create(node)
        except Exception as e:
            print(e)

        
        self.create_relationship('中药','中药分类', rels_yaocai_fenlei,'属于', '属于')
      
        return
        
    
    '''创建方剂有关节点'''
    def create_fangji(self):
        FangJi,FangJiFenLei,fangji_infos,rels_fangjiclassify,rels_yaocai_fangji = self.inputfangji()
      
        
        for fangji_dict in fangji_infos:
            try:
                node = Node("方剂", 方剂名称=fangji_dict['名称'],药用公用=fangji_dict['药用公用：'],\
                            功效主治=fangji_dict["功效主治："],方剂组成=fangji_dict["组成："],\
                            方剂出处=fangji_dict["方剂出处："],药材配方=fangji_dict["药材配方："],\
                            方剂用法=fangji_dict["方剂用法："],方剂附注=fangji_dict["方剂附注："],\
                            注意事项 ='null',方剂别名 ='null',各家论述 ='null',方剂歌诀='null',加减化裁='null',方剂鉴别='null',\
                            趣味记忆 ='null',方剂方义 ='null',方剂制法 ='null')
                self.g.create(node)
 
            except Exception as e:
                    print(e)
        
        try:
            self.create_node('方剂分类',FangJiFenLei)
        except:
            print("该节点已经存在")
       
        self.create_relationship('中药', '方剂', rels_yaocai_fangji, '入药方剂', '入药方剂')
        self.create_relationship('方剂','方剂分类',rels_fangjiclassify, '所属分类', '所属分类')
        return


if __name__ == '__main__':
    path = '39健康网1\\39健康网—整合'
    list1 = ['拔毒生肌','其他中草药','驱虫药','祛风湿药','收涩药','消食药','燥湿止痒药','止咳化痰药','开窍药','理气药','平喘药','平肝息风药','温里药','泻下药','涌吐药','止血药']
    for i in range(0,len(list1)):
        fenlei = list1[i]
        print('药材'+fenlei)
        handler = buildzhongyaodb(path,fenlei)
        #handler.delete_all()  #删除已有的全部节点，慎用！！！！
        handler.create_yaocai()
        
    for i in range(0,len(list1)):
        fenlei = list1[i]
        print('方剂'+fenlei)
        handler = buildzhongyaodb(path,fenlei)
        handler.create_fangji()
        