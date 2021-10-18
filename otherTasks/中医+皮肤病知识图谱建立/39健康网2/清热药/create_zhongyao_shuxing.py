# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 10:54:18 2021

@author: 宋小兰
"""

import json
from py2neo import Graph,Node,Relationship,NodeMatcher
graph=Graph(host='localhost',auth=('neo4j','neo4j'))
lines = []     #  第一步：定义一个列表， 打开文件
with open("清热药完整属性_end.txt",'rt',encoding="utf-8") as f:  
    for row in f.readlines(): # 第二步：读取文件内容 
        if row.strip().startswith("//"):   # 第三步：对每一行进行过滤 
            continue
        lines.append(row)                  # 第四步：将过滤后的行添加到列表中.

count=0
for i in range(2063,2919):
    matcher=NodeMatcher(graph)
    n=matcher.match("中药",id=i)
    for node in n:
        #print(node)
        #print(count)
    
    
        dict=json.loads(lines[count],strict=False)       #将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！
        #print(dict.keys())
        
        node['other_name']=dict['【别名】']
        node['pinyin_name']=dict['【汉语拼音】']
        node['chengfen']=dict['【成份】']
        node['jiagongcaiji']=dict['【加工采集】']
        node['yaocaijianbie']=dict['【药材鉴别】']
        node['gongnengzhuzhi']=dict['【功能主治】']
        node['xingwei']=dict['【性味】']
        node['yongfayongliang']=dict['【用法用量】']
        node['guijing']=dict['【归经】']
        node['zhiwuxingtai']=dict['【植物形态】']
        node['yaoyongbuwei']=dict['【药用部位】']
        node['laiziheshu']=dict['【来自何书】']
        node['mingchenying']=dict['【名称英】']
        node['yaolizuoyong']=dict['【药理作用】']
        node['paozhi']=dict['【炮制】']
        node['yiji']=dict['【宜忌】']
        node['zhucang']=dict['【贮藏】']
        node['fuzuoyong']=dict['【副作用】']
        node['lingchuangyingyong']=dict['【临床应用】']
        graph.push(node)
        print(count)
        count=count+1