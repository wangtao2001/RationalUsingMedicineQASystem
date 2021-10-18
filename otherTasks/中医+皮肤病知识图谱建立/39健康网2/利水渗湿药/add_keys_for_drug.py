# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:08:51 2021

@author: 宋小兰
"""


  
import json
lines = []     #  第一步：定义一个列表， 打开文件
with open("利水渗湿药基本属性.txt",'rt',encoding="utf-8") as f:  
    for row in f.readlines(): # 第二步：读取文件内容 
        if row.strip().startswith("//"):   # 第三步：对每一行进行过滤 
            continue
        lines.append(row)                   # 第四步：将过滤后的行添加到列表中.
count=0
dict_list=[]
for line in lines:
    dict=json.loads(line,strict=False)       #将列表中的每个字符串用某一个符号拼接为一整个字符串，用json.loads()函数加载，这样就大功告成啦！！
    count+=1
    print(count)
    #print(dict)
    
    keys_list=["【别名】","【汉语拼音】","【名称英】","【成份】","【加工采集】","【药材鉴别】","【药理作用】","【炮制】","【功能主治】","【性味】","【用法用量】","【宜忌】","【贮藏】","【副作用】","【归经】","【植物形态】","【临床应用】","【药用部位】","【来自何书】"]
    for i in keys_list:
        if i in dict.keys():
            continue
        else:
            dict[i]="null"
    #print(dict)
    dict_list.append(str(dict))
for j in dict_list:
    print(j)
    with open("利水渗湿药完整属性.txt",'a',encoding="utf-8") as f2:
        f2.write(j+'\n')
    f2.close()
     
