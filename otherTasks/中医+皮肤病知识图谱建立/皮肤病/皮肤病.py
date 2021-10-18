# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 22:03:39 2021

皮肤病
创建皮肤病节点，皮肤病与证候之间的关系，
皮肤病与方剂之间的关系
"""

from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','qazplm-55454'))

def inputData(path,datalist):
    with open(path,encoding="utf-8") as f:  
        for row in f.readlines():
            row=row.strip()
            datalist.append(row)
def create_pifubing_node(datalist):
    for row in datalist:
        try:
            node=Node("皮肤病", 皮肤病名称=row)
            graph.create(node)
        except:
            print("该节点已经存在")
def create_pifubing_shuxing(bingming,dingyi,bingyinbingli,bingzhengtedian):
    matcher=NodeMatcher(graph)
    for i in range(0,len(bingming)):
        n=matcher.match("皮肤病",皮肤病名称=bingming[i])
        for node in n:
            #print(dict(node)['皮肤病名称'])
            node['皮肤病定义']=dingyi[i]
            node['皮肤病病因病理']=bingyinbingli[i]
            node['皮肤病症状特点']=bingzhengtedian[i]
            graph.push(node) 

def bing_zheng_relationship():
    matcher=NodeMatcher(graph)  
    with open("皮肤病\\病-证.csv",encoding="gbk") as f:  

        for row in f.readlines():
            row=row.strip()
            rowDict=row.split(',')
            #print(rowDict[0])
            n=matcher.match("皮肤病",皮肤病名称=rowDict[0])
            m=matcher.match("证候",证候名称=rowDict[1])
            for node in n:
                for node1 in m:
                    n_m=Relationship(node,"病所属证候",node1)
                    graph.create(n_m)  
                    
def bing_zheng_relationship1():
    matcher=NodeMatcher(graph)  
    with open("皮肤病\\病-证.csv",encoding="gbk") as f:  
        for row in f.readlines():
            row=row.strip()
            rowDict=row.split(',')
            #print(rowDict[0])
            n=matcher.match("皮肤病",皮肤病名称=rowDict[0])
            m=matcher.match("证候分类",证候分类名称=rowDict[1])
            for node in n:
                for node1 in m:
                    n_m=Relationship(node,"病所属证候",node1)
                    graph.create(n_m)
     
def bing_fang_relationship():
    matcher=NodeMatcher(graph)
    dict2={'方剂制法':'null','方剂别名':'null','加减化裁':'null','方剂附注':'null','药用公用':'null','方剂出处':'null','药材配方':'null','各家论述':'null','方剂歌诀':'null','方剂鉴别':'null','趣味记忆':'null','方剂方义':'null'}
    with open("皮肤病\\皮肤病方剂及属性\\效验方.txt",encoding="utf-8") as f:  
        for row in f.readlines():
            row=row.strip()
            row=eval(row)
            #print(row.keys())
            try:
                node=Node("方剂", 方剂名称=row['方名'],功效主治=row['功效'],药材配方=dict2['药材配方'],
                      方剂别名=dict2['方剂别名'],方剂歌诀=dict2['方剂歌诀'],方剂出处=dict2['方剂出处'],
                      方剂组成=row['组成'],药用公用=dict2['药用公用'], 方剂附注=dict2['方剂附注'],
                      方剂制法=dict2['方剂制法'],方剂鉴别=dict2['方剂鉴别'],趣味记忆=dict2['趣味记忆'],
                      方剂方义=dict2['方剂方义'],各家论述=dict2['各家论述'],加减化裁=row['加减'],
                      方剂用法=row['用法'],注意事项=row['注意事项'])
                graph.create(node)
            except:
                print("该节点已经存在")
            n=matcher.match("皮肤病",皮肤病名称=row['病名'])
            m=matcher.match("方剂",方剂名称=row['方名'])
            for node in n:
                for node1 in m:
                    n_m=Relationship(node,"效验方",node1)
                    graph.create(n_m)
        
        
    with open("皮肤病\\皮肤病方剂及属性\\外治方.txt",encoding="utf-8") as f:  
        for row in f.readlines():
            row=row.strip()
            row=eval(row)
            #print(row['病名'])
            #print(row.keys())
            try:
                node=Node("方剂", 方剂名称=row['方名'],功效主治=row['功效'],药材配方=dict2['药材配方'],
                      方剂别名=dict2['方剂别名'],方剂歌诀=dict2['方剂歌诀'],方剂出处=dict2['方剂出处'],
                      方剂组成=row['组成'],药用公用=dict2['药用公用'], 方剂附注=dict2['方剂附注'],
                      方剂制法=row['制法'],方剂鉴别=dict2['方剂鉴别'],趣味记忆=dict2['趣味记忆'],
                      方剂方义=dict2['方剂方义'],各家论述=dict2['各家论述'],加减化裁=dict2['加减化裁'],
                      方剂用法=row['用法'],注意事项=row['注意事项'])
                graph.create(node)
            except:
                print("该节点已经存在")
            n=matcher.match("皮肤病",皮肤病名称=row['病名'])
            m=matcher.match("方剂",方剂名称=row['方名'])
            for node in n:
                for node1 in m:
                    n_m=Relationship(node,"外治方",node1)
                    graph.create(n_m)    
           
      
    with open("皮肤病\\皮肤病方剂及属性\\其他治法.txt",encoding="utf-8") as f:  
        for row in f.readlines():
            row=row.strip()
            rowDict=row.split(':')
            try:
                node=Node("其他治法", 其他治法名=rowDict[0]+'的其他治法',具体治法=rowDict[1])
                graph.create(node)
            except:
                print("该节点已经存在")
            n=matcher.match("皮肤病",皮肤病名称=rowDict[0])
            m=matcher.match("其他治法",其他治法名=rowDict[0]+'的其他治法')
            for node in n:
                for node1 in m:
                    n_m=Relationship(node,"其他治法",node1)
                    graph.create(n_m)  

def qita_fang_node(name,gongxiao,zucheng,zhifa):
    dict2={'加减化裁':'null','方剂制法':'null','注意事项':'null','方剂别名':'null','加减化裁':'null','方剂附注':'null','药用公用':'null','方剂出处':'null','药材配方':'null','各家论述':'null','方剂歌诀':'null','方剂鉴别':'null','趣味记忆':'null','方剂方义':'null'}                    
    for i in range(0,len(name)):
        try:
            node=Node("方剂", 方剂名称=name[i],功效主治=gongxiao[i],药材配方=dict2['药材配方'],
                      方剂别名=dict2['方剂别名'],方剂歌诀=dict2['方剂歌诀'],方剂出处=dict2['方剂出处'],
                      方剂组成=zucheng[i],药用公用=dict2['药用公用'], 方剂附注=dict2['方剂附注'],
                      方剂制法=dict2['方剂制法'],方剂鉴别=dict2['方剂鉴别'],趣味记忆=dict2['趣味记忆'],
                      方剂方义=dict2['方剂方义'],各家论述=dict2['各家论述'],加减化裁=dict2['加减化裁'],
                      方剂用法=zhifa[i],注意事项=dict2['注意事项'])
            graph.create(node)
        except:
            print("该节点已经存在")
            
def bing_fang_relationship1(bingming,fangji):
    matcher=NodeMatcher(graph)  
    for j in range(0,279):
        n=matcher.match("皮肤病",皮肤病名称=bingming[j])
        m=matcher.match("方剂",方剂名称=fangji[j])
        for node in n:
            for node1 in m:
                n_m=Relationship(node,"效验方",node1)
                graph.create(n_m)

            
def main():
    
    path="皮肤病\\all-病名.txt"
    bing_name=[]
    inputData(path,bing_name)
    create_pifubing_node(bing_name)
    
    path1="皮肤病\\简明皮肤病\\皮肤病名-定义.txt"
    datalist=[]
    bingming=[]
    dingyi=[]
    inputData(path1,datalist)
    for row in datalist:
        row=row.strip()
        rowDict=row.split(':')
        bingming.append(rowDict[0])
        dingyi.append(rowDict[1])
    path2="皮肤病\\简明皮肤病\\皮肤病病因病理.txt"
    bingyinbingli=[]
    inputData(path2,bingyinbingli)
    path3="皮肤病\\简明皮肤病\\皮肤病症状特点.txt"
    bingzhengtedian=[]
    inputData(path3,bingzhengtedian)
    create_pifubing_shuxing(bingming,dingyi,bingyinbingli,bingzhengtedian)
    
    path4="皮肤病\\d简明皮肤病学\\皮肤病病名-定义.txt"
    datalist1=[]
    bingming1=[]
    dingyi1=[]
    inputData(path4,datalist1)
    for row in datalist1:
        row=row.strip()
        rowDict1=row.split(':')
        bingming1.append(rowDict1[0])
        dingyi1.append(rowDict1[1])
    path5="皮肤病\\d简明皮肤病学\\皮肤病病因病理.txt"
    bingyinbingli1=[]
    inputData(path5,bingyinbingli1)
    path6="皮肤病\\d简明皮肤病学\\皮肤病症状特点.txt"
    bingzhengtedian1=[]
    inputData(path6,bingzhengtedian1)
    create_pifubing_shuxing(bingming1,dingyi1,bingyinbingli1,bingzhengtedian1)
    
    path7="皮肤病\\无属性皮肤病\\无属性皮肤病.txt"
    bingming2=[]
    datalist2=[]
    inputData(path7,datalist2)
    for row in datalist2:
        row=row.strip()
        rowDict1=row.split(':')
        bingming2.append(rowDict1[1])
    path8="皮肤病\\无属性皮肤病\\简介.txt"
    dingyi2=[]
    inputData(path8,dingyi2)
    path9="皮肤病\\无属性皮肤病\\病因病机.txt"
    bingyinbingli2=[]
    inputData(path9,bingyinbingli2)
    path10="皮肤病\\无属性皮肤病\\临床表现.txt"
    bingzhengtedian2=[]
    inputData(path10,bingzhengtedian2)
    create_pifubing_shuxing(bingming2,dingyi2,bingyinbingli2,bingzhengtedian2)
    
    bing_zheng_relationship()
    bing_zheng_relationship1()
    
    bing_fang_relationship()
    
    path11="皮肤病\\皮肤病方剂及属性\\方剂名.txt"
    name=[]
    inputData(path11,name)
    path12="皮肤病\\皮肤病方剂及属性\\功效.txt"
    gongxiao=[]
    inputData(path12,gongxiao)
    path13="皮肤病\\皮肤病方剂及属性\\组成.txt"
    zucheng=[]
    zhifa=[]
    datalist3=[]
    inputData(path13,datalist3)
    for row in datalist3:
        row=row.strip()
        rowDict=row.split('制剂用法：')
        zhifa.append(rowDict[1])
        zucheng.append(rowDict[0])
    qita_fang_node(name,gongxiao,zucheng,zhifa)
    
    path14="皮肤病\\皮肤病方剂及属性\\病名.txt"
    bingming3=[]
    inputData(path14,bingming3)
    path15="皮肤病\\皮肤病方剂及属性\\病对应方剂名.txt"
    fangji=[]
    inputData(path15,fangji)
    bing_fang_relationship1(bingming3,fangji)
main()
    