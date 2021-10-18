# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 15:01:50 2021

39健康网部分中药，方剂节点，中药与中药分类间的关系，
方剂与方剂分类间的关系，中药与方剂之间的关系，
十八反，十九畏
"""

from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','qazplm-55454'))

def inputData(path,datalist):
    with open(path,encoding="utf-8") as f:
        for row in f.readlines():
            row=row.strip()
            datalist.append(row)
            
def createZhongyao_node(count,datalist1,datalist2):
    for i in datalist2:
        yaocai_dict=eval(i)
        try:
            node = Node("中药", 中药名称=datalist1[count],中药拼音=yaocai_dict['【汉语拼音】'],\
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
            graph.create(node)
            print(count)
        except:
            print("该节点已经存在")
        count=count+1
def createFangji_node(count,datalist1,datalist2):
    namelist=[]
    for j in datalist1:
        try:
            node=Node("方剂",方剂名称=j)
            graph.create(node)
            namelist.append(j)
        except:
            print("该节点已经存在")
    count=0
    dict2={'方剂制法':'null','注意事项':'null','方剂别名':'null','各家论述':'null','方剂歌诀':'null','加减化裁':'null','方剂鉴别':'null','趣味记忆':'null','方剂方义':'null'}
    matcher=NodeMatcher(graph)
    for name in namelist:
        dict1=eval(datalist2[count])
        n=matcher.match("方剂",方剂名称=name)
        for node in n:
            #print(dict(node)['方剂名称'])
            node['方剂别名']=dict2['方剂别名']
            node['方剂出处']=dict1['方剂出处：']
            node['方剂歌诀']=dict2['方剂歌诀']
            node['方剂组成']=dict1['组成：']
            node['方剂用法']=dict1['方剂用法：']
            node['功效主治']=dict1['功效主治：']
            node['加减化裁']=dict2['加减化裁']
            node['药材配方']=dict1['药材配方：']
            node['药用公用']=dict1['药用公用：']
            node['方剂附注']=dict1['方剂附注：']
            node['方剂制法']=dict2['方剂制法']
            node['方剂鉴别']=dict2['方剂鉴别']
            node['趣味记忆']=dict2['趣味记忆']
            node['方剂方义']=dict2['方剂方义']
            node['各家论述']=dict2['各家论述']
            node['注意事项']=dict2['注意事项']
            graph.push(node)
        print(count)
        count=count+1 

def create_yao_fenlei_node(list1):
    for j in list1:
        try:
            node=Node("中药分类",中药分类名称=j)
            graph.create(node)
        except:
            print("该节点已经存在")

def create_fangji_fenlei(fangjifenlei):
    list2=[]
    for i in fangjifenlei:
        if i not in list2:
            list2.append(i)
    for j in list2:
        try:
            node=Node("方剂分类",方剂分类名称=j)
            graph.create(node)
        except:
            print("该节点已经存在")
            

            
def shibanfan_relationship(list1,list2):
    matcher=NodeMatcher(graph)     
    for i in range(0,53):
        m=matcher.match("中药", 中药名称=list1[i])
        n=matcher.match("中药", 中药名称=list2[i])
        for node in m:
            print(dict(node)['中药名称'])
            for node1 in n:
                print(dict(node1)['中药名称'])
                n_m=Relationship(node,"反",node1)
                graph.create(n_m)

def shijiuwei_relationship():
    yao_name_list=[]
    wei1=[]
    wei2=[]
    with open("39健康网2\\十九畏.txt",encoding="utf-8") as f:  
        for row in f.readlines():
            row=row.strip()
            yao_name_list.append(eval(row))
    for i in yao_name_list:
        #print(i)
        for j in i:
            #print(j[0])
            #print(j[1])
            wei1.append(j[0])
            wei2.append(j[1])
    matcher=NodeMatcher(graph) 
    for i in range(0,10):
        m=matcher.match("中药", 中药名称=wei1[i])
        n=matcher.match("中药", 中药名称=wei2[i])
        for node in m:
            print(dict(node)['中药名称'])
            for node1 in n:
                print(dict(node1)['中药名称'])
                m_n=Relationship(node,"畏",node1)
                graph.create(m_n)
            
def fang_fangfenlei_Relationship(list1,list2):
    matcher=NodeMatcher(graph)
    rel_zhengfangs = []
    for i in range(0,len(list1)):
        m=matcher.match("方剂", 方剂名称=list1[i])
        n=matcher.match("方剂分类",方剂分类名称=list2[i])
        print(m)
        rel_zhengfangs.append([m,n])
    return rel_zhengfangs      

def yao_fenlei(fenlei_name,datalist):
    matcher=NodeMatcher(graph)  
    m=matcher.match("中药分类",中药分类名称=fenlei_name)
    for node in m:
        for count1 in datalist:
            n1=matcher.match("中药",中药名称=count1)
            for node1 in n1:
                #print(node1)
                n1_m=Relationship(node1,"属于",node)
                graph.create(n1_m)
        
             
def yao_fangji_createRelationship(list1,list2):
    matcher=NodeMatcher(graph)
    for i in range(0,len(list1)):
        m=matcher.match("中药", 中药名称=list1[i])
        n=matcher.match("方剂",方剂名称=list2[i])
        for node in m:
            print(dict(node)['中药名称'])
            for node1 in n:
                print(dict(node1)['方剂名称'])           
                n_m=Relationship(node,"入药方剂",node1)
                graph.create(n_m)

def create_relationship(start_node, end_node, edges, rel_type, rel_name):
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
           graph.run(query)
        except Exception as e:
            print(e)
    return
        
def main():
  
    path1="39健康网2\\yao_name1.txt"
    zhongyaolist=[]
    inputData(path1, zhongyaolist)
    path2="39健康网2\\new_shuxing.txt"
    zhongyaoshuxing=[]
    inputData(path2, zhongyaoshuxing)
    count=0
    createZhongyao_node(count, zhongyaolist, zhongyaoshuxing)

    path3="39健康网2\\入药方剂_name_new.txt"
    path4="39健康网2\\入药方剂_属性_new.txt"
    fangjilist=[]
    fangjishuxing=[]
    inputData(path3, fangjilist)
    inputData(path4, fangjishuxing)
    createFangji_node(count, fangjilist, fangjishuxing)
     
    path5="39健康网2\\all_yao_name.txt"
    path6="39健康网2\\all_fangji_name.txt"
    list1=[]
    list2=[]
    inputData(path5, list1)
    inputData(path6, list2)
    rel_yaofangs = []
    for i in range(0,len(list1)):
        m = list1[i]
        n = list2[i]
        rel_yaofangs.append([m,n]) 
    create_relationship('中药', '方剂',rel_yaofangs, '入药方剂', '入药方剂')

    path7="39健康网2\\分类.txt"
    fenleilist=[]
    inputData(path7, fenleilist)
    create_yao_fenlei_node(fenleilist)
    
    path8="39健康网2\\入药方剂_分类.txt"
    fangjifenlei=[]
    inputData(path8, fangjifenlei)
    create_fangji_fenlei(fangjifenlei)
    rel_fangsfenlei = []
    for i in range(0,len(fangjilist)):
        m = fangjilist[i]
        n = fangjifenlei[i]
        rel_fangsfenlei.append([m,n]) 
    create_relationship('方剂', '方剂分类',rel_fangsfenlei, '所属分类', '所属分类')
   
    path9="39健康网2\\shibafan1.txt"
    path10="39健康网2\\shibafan2.txt"
    fan1=[]
    fan2=[]
    inputData(path9, fan1)
    inputData(path10, fan2)
    shibanfan_relationship(fan1,fan2)
    
    shijiuwei_relationship()

    path11="39健康网2\\安神药\名称.txt"
    ansheng_list=[]
    inputData(path11, ansheng_list)
    fenlei_name='安神药'
    yao_fenlei(fenlei_name,ansheng_list)
    path12="39健康网2\\补虚药\yaocai.txt"
    buxu_list=[]
    inputData(path12, buxu_list)
    fenlei_name='补虚药'
    yao_fenlei(fenlei_name,buxu_list)
    path13="39健康网2\\芳香化湿药\名称.txt"
    fangxiang_list=[]
    inputData(path13, fangxiang_list)
    fenlei_name='芳香化湿药'
    yao_fenlei(fenlei_name,fangxiang_list)
    path14="39健康网2\\活血化瘀药\名称.txt"
    huoxue_list=[]
    inputData(path14, huoxue_list)
    fenlei_name='活血化瘀药'
    yao_fenlei(fenlei_name,huoxue_list)
    path15="39健康网2\\解表药\名称.txt"
    jiebiao_list=[]
    inputData(path15, jiebiao_list)
    fenlei_name='解表药'
    yao_fenlei(fenlei_name,jiebiao_list)
    path16="39健康网2\\解毒杀虫药\名称.txt"
    jiedu_list=[]
    inputData(path16, jiedu_list)
    fenlei_name='解毒杀虫药'
    yao_fenlei(fenlei_name,jiedu_list)
    path17="39健康网2\\利水渗湿药\名称.txt"
    lishui_list=[]
    inputData(path17, lishui_list)
    fenlei_name='利水渗湿药'
    yao_fenlei(fenlei_name,lishui_list)
    path18="39健康网2\\清热药\清热药药名_name.txt"
    qingre_list=[]
    inputData(path18, qingre_list)
    fenlei_name='清热药'
    yao_fenlei(fenlei_name,qingre_list)

  
main()