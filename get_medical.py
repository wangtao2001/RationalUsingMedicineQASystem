# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/04/06, Mon

import requests
from bs4 import BeautifulSoup

start_url = "https://ybk.39.net/"
headers = {r"user-agent": "Mozilla\5.0"}

'''
with open(r".\data\medical_url.txt",'r',encoding='utf-8') as medical_url_f:
    medical_url_list_tp = [eval(url) for url in medical_url_f.readlines()]  # 每个元素都是字典
medical_url_list = [di[key] for di in medical_url_f for key in di.keys()]  # 所有药品url的列表
'''
# 示例list
medical_url_list = ['http://ypk.39.net/2027184/', 'http://ypk.39.net/2029556/']

medical_f = open(r".\substance\medical.txt",'a',encoding='utf-8')  # medical实体文件

for url in medical_url_list:
    medical_dict = dict()
    url += "manual/"

    r = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(r.content, 'html.parser')

    medical_dict["id"] = url[18:-8]  # 写入唯一标识符

    medical_f.write(str(medical_dict))  # txt文件将会包药品 medical实体字典
    medical_f.write("\n")
medical_f.close()




