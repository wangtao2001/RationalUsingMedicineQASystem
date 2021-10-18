# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 09:58:47 2021

@author: 宋小兰
"""


from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','neo4j'))
'''
dict2={'加减化裁':'null','方剂制法':'null','注意事项':'null','方剂别名':'null','加减化裁':'null','方剂附注':'null','药用公用':'null','方剂出处':'null','药材配方':'null','各家论述':'null','方剂歌诀':'null','方剂鉴别':'null','趣味记忆':'null','方剂方义':'null'}
name=[]
with open("方剂名.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        name.append(row)
        
gongxiao=[]
with open("功效.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        gongxiao.append(row)

zucheng=[]
zhifa=[]
count=0
with open("组成.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        rowDict=row.split('制剂用法：')
        zhifa.append(rowDict[1])
        zucheng.append(rowDict[0])
        
for i in range(0,254):
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
'''
bingming=[]
with open("病名.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        bingming.append(row)
        
fangji=[]
with open("病对应方剂名.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        fangji.append(row)
matcher=NodeMatcher(graph)  
for j in range(0,279):
    n=matcher.match("皮肤病",皮肤病名称=bingming[j])
    m=matcher.match("方剂",方剂名称=fangji[j])
    for node in n:
        for node1 in m:
            n_m=Relationship(node,"效验方",node1)
            graph.create(n_m)
