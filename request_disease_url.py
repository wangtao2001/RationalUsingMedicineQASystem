# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/04/03, Sat

import requests
import json
import time
from bs4 import BeautifulSoup

li = []  # 去重列表

start_url = "https://jbk.39.net/bw/"
headers = {r"user-agent": "Mozilla\5.0"}

with open(r".\data\department.json", "r", encoding="utf-8") as department_f:
    department_dict = json.load(department_f, encoding="utf-8")
url_list = [start_url + de for key in department_dict.keys() for de in department_dict[key]]

disease_url_f = open(r".\data\disease_url.txt", "a", encoding="utf-8")  # 追加写

disease_url_dict = dict()
for url in url_list:  # url_list长度为41 索引0:41

    r1 = requests.get(url, headers=headers, timeout=15)
    soup1 = BeautifulSoup(r1.content, "html.parser")

    ul = soup1.find_all("ul", attrs={"class": "result_item_dots"})[0]
    page_num = int(ul.find_all("a")[-2].string)  # 页数

    for i in range(1, page_num + 1):  # 每个科室下的每一页
        r1 = requests.get(url + f'_p{i}', headers=headers, timeout=15)
        soup2 = BeautifulSoup(r1.content, "html.parser")

        div_list = soup2.find_all("div", attrs={"class": "result_item"})
        for div in div_list:
            span = div.find_all("span")[0]
            if span.string == "疾病":  # 而非症状、检查...
                disease_name = div.find_all("a")[0].get("title")
                href = div.find_all("a")[0].get("href")

                if href not in li:  # 还未添加过
                    li.append(href)

                    disease_url_dict[disease_name] = href
                    print(disease_name)

                    disease_url_f.write(str(disease_url_dict))  # txt文件将会包含很多字典，每一个字典仅包含一个键值对 疾病：url
                    disease_url_f.write("\n")
                disease_url_dict = dict()

disease_url_f.close()
