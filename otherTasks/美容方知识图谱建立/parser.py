import json
import re
import sys

with open('./data_backup.json','r',encoding='utf8')as fp:
    data = json.load(fp)

def parser(s:str):
    li = s.split(',')
    result = {}
    for item in li:
        if '、' in item:
            try:
                content = re.search(r'各((等份)|(少许)|(\d+克)|(\d+枚)|(\d+挺)|(\d+具)|(\d+合)|(\d+升)|(少许)|(适量)|(\d+毫升))',item).group()
            except AttributeError:
                print(s)
                sys.exit()
            item = item.replace(content, '')
            content = content.replace('各','')
            drugs = item.split('、')
            for drug in drugs:
                result[drug] = content
        else: # 就是一个药物xx克
            try:
                content = re.search(r'(\d+克)|(\d+枚)|(\d+挺)|(\d+具)|(\d+合)|(\d+升)|(少许)|(适量)|(\d+毫升)',item).group()
            except AttributeError:
                print(s)
                sys.exit()
            drug = item.replace(content, '')
            result[drug] = content
    return result


for i in range(4):
    for j in range(len(data[i]['内治方'])):
        s = data[i]['内治方'][j]['组成']
        result = parser(s)
        data[i]['内治方'][j]['组成'] = result
    for j in range(len(data[i]['外治方'])):
        s = data[i]['外治方'][j]['组成']
        result = parser(s)
        data[i]['外治方'][j]['组成'] = result

# data

with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)
    print("write json file success!")
