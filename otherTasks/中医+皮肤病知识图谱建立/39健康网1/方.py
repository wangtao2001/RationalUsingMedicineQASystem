# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:12:45 2021

@author: 宋小兰
"""


from py2neo import Graph,Node,Relationship,NodeMatch
graph=Graph(host='localhost',auth=('neo4j','qazplm-55454'))
    
mingcheng=[]
count=0
with open("39健康网1\\biaogefangji_name.txt",encoding="utf-8") as f:  
    for row in f.readlines():
        row=row.strip()
        mingcheng.append(row)
        '''
mingcheng1=[]
for j in mingcheng:
    if not j in mingcheng1:
        mingcheng1.append(j)'''

dict1={'方剂出处':'null','方剂组成':'null','方剂用法':'null','功效主治':'null','药材配方':'null','药用公用':'null','方剂附注':'null'}
dict2={'方剂制法':'null','注意事项':'null','方剂别名':'null','各家论述':'null','方剂歌诀':'null','加减化裁':'null','方剂鉴别':'null','趣味记忆':'null','方剂方义':'null'}
for i in mingcheng:
    try:
        node=Node("方剂", 方剂名称=mingcheng[count],方剂别名=dict2['方剂别名'],方剂出处=dict1['方剂出处：'],方剂歌诀=dict2['方剂歌诀'],
    方剂组成=dict1['组成：'],
    方剂用法=dict1['方剂用法：'],
    功效主治=dict1['功效主治：'],
    加减化裁=dict2['加减化裁'],
    药材配方=dict1['药材配方：'],
    药用公用=dict1['药用公用：'],
    方剂附注=dict1['方剂附注：'],
    方剂制法=dict2['方剂制法'],
    方剂鉴别=dict2['方剂鉴别'],
    趣味记忆=dict2['趣味记忆'],
    方剂方义=dict2['方剂方义'],
    各家论述=dict2['各家论述'],
    注意事项=dict2['注意事项'])
        graph.create(node)
        print(count)
    except:
        print("该节点已经存在")
    count=count+1

    
        
                
                
