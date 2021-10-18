# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 14:43:21 2021

@author: 独顽似鄙
"""

from py2neo import Graph,Node,Relationship,NodeMatcher
from py2neo.matching import *

class buildzhongyaodb:
    def __init__(self):
        username = 'neo4j'
        password = 'qazplm-55454'
        self.g = Graph('http://localhost:7474/', auth=(username, password))
        
    def delete_all(self):
      self.g.delete_all()
    
    def inputdata(self):
        with open("医药查询平台\\drug_total_new1.txt","r",encoding = "utf-8") as f:
            drugs = [eval(dict) for dict in f.readlines()]
            
            rels_drug = []
            rels_yaocai_fangji =[]
            for drug_dict in drugs:
                if drug_dict['relatedDrug'] != "null":
                    drugname = drug_dict['relatedDrug'].split('、')
                    for i in drugname:
                        rels_drug.append([drug_dict['chineseName'],i]) #中药 -----> 西药
                
                if drug_dict['relatedPrescription'] != "null":
                    fangjiname = drug_dict['relatedPrescription'].split('、')
                    for i in fangjiname:
                        rels_yaocai_fangji.append([drug_dict['chineseName'],i]) #中药  ------>方剂
       

        return drugs,rels_drug,rels_yaocai_fangji

    
    def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
        # 去重处理
        set_edges = []
        for edge in edges:
            set_edges.append('###'.join(edge))
            
        for edge in set(set_edges):
            edge = edge.split('###')
            p = edge[0]
            q = edge[1]
            
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" % (
                start_node, end_node, p, q, rel_type, rel_name)
            try:
                self.g.run(query)
            except Exception as e:
                print(e)
        return
    
    
    '''创建药材有关节点'''
    def create_drug_node(self):
        Drugs,rels_drug,rels_yaocai_fangji = self.inputdata()
      
        #different
        for drugs_dict in Drugs:
            try:
                node = Node("中药", 中药名称=drugs_dict ['chineseName'],中药拼音=drugs_dict ['chinesePinyin'],\
                            加工采集=drugs_dict ['harvestProcess'],化学成分=drugs_dict ['chemicalComposition'],\
                            功能主治=drugs_dict ['func']+drugs_dict ['mainAttend'],用法用量=drugs_dict ['dosage'],\
                            形态特征=drugs_dict ['Frature'],药用部位=drugs_dict['drugSite'],中药英文名= 'null',\
                            中药鉴别=drugs_dict ['identify'],药理作用=drugs_dict ['pharmacology'],\
                            炮制方法=drugs_dict ['processing'],中药宜忌=drugs_dict ['taboo'],中药出处=drugs_dict ['relatedDiscussion'] ,\
                            保存方法=drugs_dict ['storageMethod'],副作用=drugs_dict ['adverseReactions'],\
                            临床应用=drugs_dict ['clinicalApplication'],中药别名=drugs_dict ['alisaName'],\
                            性味归经=drugs_dict ['remark'],毒理作用=drugs_dict ['toxicologicalEffects'],\
                            饮片性状=drugs_dict ['decoctionPiecesCharacter'] ,常见伪品=drugs_dict ['comCounterfeit'],\
                            药材性状=drugs_dict['medicinalProperty'] ,饮片名称=drugs_dict ['herbalPiecesName'] ,\
                            注意事项=drugs_dict ['notice'],相关配伍=drugs_dict ['configuration'],鉴别用药=drugs_dict ['identifyMedication'],\
                            分布区域=drugs_dict['CropArea'],医保类型=drugs_dict ['healthType'],植物信息=drugs_dict ['plant'] ,中药附注=drugs_dict ['notes'],\
                            道地产区=drugs_dict ['RealEstate'],中药种属=drugs_dict ['Genus'],生长环境=drugs_dict ['GrowthEnvironment'],\
                            繁殖方式=drugs_dict['sireMethods'],成份检验=drugs_dict['contentPic'],\
                            药品检验=drugs_dict['pharmacyCheck'],中药简介=drugs_dict ['intro'],中药拉丁名=drugs_dict ['latinName'],\
                            中药毒性=drugs_dict ['toxicity'],现代研究=drugs_dict ['modernResearch'],药膳食疗=drugs_dict ['dietGuidelines']) 
                self.g.create(node)
               
            except Exception as e:
                print(e)
        
        return
        

if __name__ == '__main__':
    
        handler = buildzhongyaodb()
        #handler.delete_all()  #删除已有的全部节点，慎用！！！！
           
        handler.create_drug_node()
        
        
        