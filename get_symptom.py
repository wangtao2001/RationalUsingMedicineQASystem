# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author: wangtao
# @create on: 21/04/10, Sat

import requests
from bs4 import BeautifulSoup

start_url = "https://jbk.39.net/zq/zhengzhuang"
headers = {r"user-agent": "Mozilla\5.0"}

if __name__ == "__main__":
    with open(r".\data\symptom_url.txt", 'r', encoding='utf-8') as symptom_url_f:
        symptom_url_list_tp = [eval(url) for url in symptom_url_f.readlines()]  # 每个元素都是字典
    symptom_url_list = [di[key] for di in symptom_url_list_tp for key in di.keys()]  # 所有症状url的列表

    symptom_f = open(r".\substance\symptom.txt", 'a', encoding='utf-8')  # symptom实体文件

    count = 0  # 计数器
    # 前10条测试数据
    for url in symptom_url_list[:10]:
        count += 1
        print(count)

        symptom_dict = {}
        
        symptom_f.write(str(symptom_dict))  # txt文件将会保存药品 medical实体字典
        symptom_f.write("\n")
    symptom_f.close()
