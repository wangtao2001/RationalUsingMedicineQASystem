# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/04/03, Sat

import requests
import bs4
from bs4 import BeautifulSoup

count = 0

start_url = "https://jbk.39.net/"
headers = {r"user-agent": "Mozilla\5.0"}

with open(r".\data\disease_url.txt", 'r', encoding='utf-8') as disease_url_f:
    disease_url_list_tp = [eval(url) for url in disease_url_f.readlines()]  # 每个元素都是字典
disease_url_list = [di[key] for di in disease_url_list_tp for key in di.keys()]  # 所有疾病的列表

disease_f = open(r'.\substance\disease.txt', 'a', encoding='utf-8')  # 追加写
symptom_url_f = open(r".\data\symptom_url.txt", 'a', encoding='utf-8')  # 所有症状url
check_url_f = open(r".\data\check_url.txt", 'a', encoding='utf-8')  # 所有检查url
medical_url_f = open(r".\data\medical_url.txt", 'a', encoding='utf-8')  # 所有药品url

for url in disease_url_list[count:]:  # 15179 条数据

    count += 1
    i = int(int(100 * count / 15179) / 2)
    print("\r" + str(count) + "|" + "█" * i + " " * (50 - i) + "|" + "{:.2f}%".format(100 * count / 15179),
          end='')  # 刷新输出显示百分比进度

    disease_dict = dict()

    r1 = requests.get(url, headers=headers, timeout=15)
    soup1 = BeautifulSoup(r1.content, 'html.parser')

    # =====================基本属性BEGIN===================
    disease_dict['id'] = url[19:-1]  # 写入唯一标识符
    disease_name = soup1.find("div", attrs={"class": "disease"}).find("h1").string
    disease_dict['name'] = disease_name  # 写入疾病名称

    li_list = soup1.find("ul", attrs={"class": "information_ul"}).find_all("li")

    for li in li_list:
        if li.find("i").string[:-1] == "别名":  # 写入别名
            disease_dict["another_name"] = li.find("span").string.strip()
            break
    else:
        disease_dict["another_name"] = None

    for li in li_list:
        if li.find("i").string[:-1] == "是否医保":  # 写入是否医保
            disease_dict["insurance"] = li.find("span").string.strip()
            break
    else:
        disease_dict["insurance"] = None

    for li in li_list:
        if li.find("i").string[:-1] == "发病部位":  # 写入发病部位
            try:
                disease_dict["site"] = li.find("a").string.strip()
            except:
                break
    else:
        disease_dict["site"] = None

    for li in li_list:
        if li.find("i").string[:-1] == "多发人群":  # 写入多发人群
            disease_dict["people"] = li.find("span").string.strip()
            break
    else:
        disease_dict["people"] = None

    for li in li_list:
        if li.find("i").string[:-1] == "治愈率":  # 写入治愈率
            disease_dict["ure_rate"] = li.find("span").string.strip()
            break
    else:
        disease_dict["cure_rate"] = None

    for li in li_list:
        if li.find("i").string[:-1] == "挂号科室":  # 写入挂号科室
            try:
                disease_dict["department"] = li.find("a").string.strip()
            except:
                disease_dict["department"] = None
                break
    else:
        disease_dict["department"] = None

    des_url = url + "jbzs/"
    r2 = requests.get(des_url, headers=headers, timeout=15)
    soup2 = BeautifulSoup(r2.content, 'html.parser')
    try:
        des = soup2.find("p", attrs={"class": "introduction"}).string
        disease_dict["description"] = des  # 写入简介
    except:
        disease_dict["description"] = None
    # ========================END=====================

    # =====================关系BEGIN===================
    for li in li_list:
        if li.find("i").string[:-1] == "典型症状":
            symptom_list = []
            symptom_url_dict = {}
            a_list = li.find_all('a')
            for a in a_list:
                symptom_list.append(a.get("href")[31:-1])  # 外码 症状的id
                symptom_url_dict[a.get("title")] = a.get("href")
                symptom_url_f.write(str(symptom_url_dict))
                symptom_url_f.write("\n")
                symptom_url_dict = {}  # 写入症状url
            disease_dict["symptom"] = symptom_list
            break
    else:
        disease_dict["symptom"] = None

    for li in li_list:
        if li.find("i").string[:-1] == "临床检查":
            check_list = []
            check_url_dict = {}
            a_list = li.find_all('a')
            for a in a_list:
                check_list.append(a.get("href")[27:-1])  # 外码 检查的id
                check_url_dict[a.get("title")] = a.get("href")
                check_url_f.write(str(check_url_dict))
                check_url_f.write("\n")
                check_url_dict = {}  # 写入检查url
            disease_dict["check"] = check_list
            break
    else:
        disease_dict["check"] = None

    for li in li_list:
        if li.find("i").string[:-1] == "并发症":
            disease_list = []
            a_list = li.find_all('a')
            for a in a_list:
                disease_list.append(a.get("href")[19:-1])  # 外码 并发症的id
            disease_dict["disease"] = disease_list
            break
    else:
        disease_dict["disease"] = None

    li = soup1.find("ul", attrs={"class": "information_ul information_ul_bottom"}).find("li")
    if li.find("i").string[:-1] == "常用药品":
        medical_list = []
        medical_url_dict = {}
        a_list = li.find_all('a')

        for a in a_list:
            medical_list.append(a.get("href")[18:-1])  # 外码 常用药品的id
            medical_url_dict[a.string] = a.get("href")
            medical_url_f.write(str(medical_url_dict))
            medical_url_f.write("\n")
            medical_url_dict = {}
        disease_dict["medical"] = medical_list
    else:
        disease_dict["medical"] = None
    # ========================END=====================
    disease_f.write(str(disease_dict))  # txt文件将会包含很多字典，每一个字典仅包含一个实体：疾病 disease
    disease_f.write("\n")

disease_f.close()
symptom_url_f.close()
check_url_f.close()
medical_url_f.close()

