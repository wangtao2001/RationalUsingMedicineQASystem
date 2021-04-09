# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author: wangtao
# @data: 21/04/06, Mon

import requests
from bs4 import BeautifulSoup

count = 0  # 计数器

start_url = "https://ybk.39.net/"
headers = {r"user-agent": "Mozilla\5.0"}

with open(r".\data\medical_url.txt", 'r', encoding='utf-8') as medical_url_f:
    medical_url_list_tp = [eval(url) for url in medical_url_f.readlines()]  # 每个元素都是字典
medical_url_list = [di[key] for di in medical_url_list_tp for key in di.keys()]  # 所有药品url的列表

medical_f = open(r".\substance\medical.txt", 'a', encoding='utf-8')  # medical实体文件

# 测试用10条数据
for url in medical_url_list[:10]:  # 6702条数据 无重复 index = 0:6702
    count += 1
    print(count)

    medical_dict = dict()
    url += "manual/"

    r = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(r.content, 'html.parser')

    medical_dict["id"] = url[18:-8]  # 写入唯一标识符
    medical_dict['is_recipe'] = soup.find("i", attrs={"class": "drug-layout-r-icon1"}).string  # 写入是否处方

    ul = soup.find("ul", attrs={"class": "drug-explain"})
    li_list = ul.find_all("li")

    # 药品名称 name（通用名称、商品名称、英文名称、汉语拼音）
    for li in li_list:
        if li.find("p", attrs={"class": "drug-explain-tit"}).string[1:-1] == "药品名称":
            name_list = [s.strip() for s in li.find("p", attrs={"class": "drug-explain-txt"}).get_text().strip().split('\n')]  # 包含各种name的列表
            # 首先全设为None,能够找到的再修改
            medical_dict.update({"normal_name": None, "product_name": None, "en_name": None, "pinyin_name": None})
            for name in name_list:
                if name[:4] == "通用名称":
                    medical_dict["normal_name"] = name.split("：")[1]
                elif name[:4] == "商品名称":
                    medical_dict["product_name"] = name.split("：")[1]
                elif name[:4] == "英文名称":
                    medical_dict["en_name"] = name.split("：")[1]
                elif name[:4] == "汉语拼音":
                    medical_dict["pinyin_name"] = name.split("：")[1]
                else:
                    pass
            break

    # 成分 ingredient
    for li in li_list:
        if li.find("p", attrs={"class": "drug-explain-tit"}).string[1:-1] == "成份":
            ingredient = li.find("p", attrs={"class": "drug-explain-txt"}).text.strip()
            # 文字中可能含有p和br标签
            medical_dict["ingredient"] = ingredient.lstrip("<p>").rstrip("</p>").replace("<br />","").replace("\n","。")
            break
        else:
            medical_dict["ingredient"] = None

    medical_f.write(str(medical_dict))  # txt文件将会保存药品 medical实体字典
    medical_f.write("\n")
medical_f.close()
