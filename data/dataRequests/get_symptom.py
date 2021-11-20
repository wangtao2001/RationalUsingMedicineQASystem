# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author: wangtao
# @create on: 21/04/10, Sat

import requests
from bs4 import BeautifulSoup

start_url = "https://jbk.39.net/zq/zhengzhuang"
headers = {r"user-agent": "Mozilla\5.0"}

if __name__ == "__main__":
    with open(r"../data/symptom_url.txt", 'r', encoding='utf-8') as symptom_url_f:
        symptom_url_list_tp = [eval(url) for url in symptom_url_f.readlines()]  # 每个元素都是字典
    symptom_url_list = [di[key] for di in symptom_url_list_tp for key in di.keys()]  # 所有症状url的列表

    symptom_f = open(r"../substance/symptom.txt", 'a', encoding='utf-8')  # symptom实体文件

    count = 3477  # 计数器
    for url in symptom_url_list[count:]: # 4007条数据
        count += 1
        print(count)

        symptom_dict = {"id": url[31:-1]} # 初始化字典、写入唯一标识符

        r = requests.get(url,headers=headers,timeout=15)
        soup = BeautifulSoup(r.content,'html.parser')

        symptom_dict["name"] = soup.find("h1").text # 写入症状名称
        symptom_dict["describe"] = soup.find("dd",attrs={"id":"intro"}).find("p").get_text().replace("\u3000","").replace("\n","")  # 写入症状描述

        r2 = requests.get(url+"zzqy/",headers=headers,timeout=15)
        soup2 = BeautifulSoup(r2.content,'html.parser')

        symptom_dict["cause"] = soup2.find("div",attrs={"class":"item catalogItem"}).get_text().replace("\u3000","").replace("\n","").replace("\xa0","")  # 写入症状起因

        try:
            r3 = requests.get(url+"jzzn/",headers=headers,timeout=8) # 有的症状会有就诊指南
            r3.raise_for_status()
        except:
            symptom_dict["department"] = None # 就诊科室
            symptom_dict["related"] = None # 易混淆症状
            symptom_dict["interrogation"] = None # 问诊内容
        else:
            soup3 = BeautifulSoup(r3.content,'html.parser')
            dl_list = soup3.find("div", attrs={"id": 'contentText'}).find_all("dl")

            for dl in dl_list:
                if dl.find("dt").string == "建议就诊科室":
                    symptom_dict["department"] = dl.find("dd").string
                    break
                else:
                    symptom_dict["department"] = None
            for dl in dl_list:
                if dl.find("dt").string == "易混淆症状":
                    symptom_dict["related"] = dl.find("dd").string
                    break
                else:
                    symptom_dict["related"] = None
            for dl in dl_list:
                if dl.find("dt").string == "常见问诊内容":
                    inter = "".join([dd.string.replace("\n","") for dd in dl.find_all("dd") if dd.string is not None])
                    symptom_dict["interrogation"] = inter
                    break
                else:
                    symptom_dict["interrogation"] = None

        disesae_list = [] # 相关疾病
        try:
            a_list = soup.find("table",attrs={"class":"dis"}).find_all("a")
        except:
            symptom_dict["disease"] = []
        else:
            for a in a_list:
                if a.get("href")[:19] == "https://jbk.39.net/":
                    disesae_list.append(a.get("href")[19:-1])
            symptom_dict["disease"] = disesae_list

        check_list = []  # 鉴别检查
        r4 = requests.get(url+"jcjb/",headers=headers,timeout=15)
        soup4 = BeautifulSoup(r4.content,'html.parser')
        div = soup4.find("div",attrs={"class":"checkbox-data"})
        if div is not None:
            a_list = []
            tr_list = div.find_all("tr",recursive=True)
            if tr_list is not None:
                for tr in tr_list:
                    a_list.append(tr.find("a",recursive=True))
        for a in a_list:
            if a is not None and a.get("href")[:27] == "https://jbk.39.net/jiancha/":
                check_list.append(a.get("href")[27:-1])
        symptom_dict["check"] = check_list

        symptom_f.write(str(symptom_dict))  # txt文件将会保存药品 medical实体字典
        symptom_f.write("\n")
    symptom_f.close()
