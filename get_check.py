# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author: wangtao
# @create on: 21/04/10, Sat

import requests
from bs4 import BeautifulSoup

start_url = "https://jbk.39.net/jiancha/"
headers = {r"user-agent": "Mozilla\5.0"}

if __name__ == "__main__":
    with open(r".\data\check_url.txt", 'r', encoding='utf-8') as check_url_f:
        check_url_list_tp = [eval(url) for url in check_url_f.readlines()]  # 每个元素都是字典
    check_url_list = [di[key] for di in check_url_list_tp for key in di.keys()]  # 所有检查url的列表

    check_f = open(r".\substance\check.txt", 'a', encoding='utf-8')  # medical实体文件

    count = 1989
    # 10条测试数据
    for url in check_url_list[count:]:  # 2189 条检查无重复 index=0:2189
        count += 1
        print(count)

        check_dict = dict()  # 属性字典
        check_dict["id"] = url[27:-1]  # 写入唯一标识符

        r = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(r.content, 'html.parser')

        name = soup.find("div", attrs={"class": "main wrap"}).find("div", attrs={"class": "ss_det catalogItem"},
                                                                   recursive=False).find("b").get_text()
        check_dict["name"] = name  # 写入检查名称

        describe = soup.find("div", attrs={"id": "intro"}).get_text().rstrip("...[详细][收起]").lstrip().replace("　　", "")
        check_dict["describe"] = describe  # 写入检查介绍

        ul = soup.find("ul", attrs={"class": "infolist"})
        li_list = ul.find_all("li", recursive=False)

        for li in li_list:
            if li.find("b").string[:-1] == "检查部位":
                site = li.get_text().strip().replace("\n", " ")[6:]
                check_dict["site"] = site
                break
            else:
                check_dict["site"] = None

        for li in li_list:
            if li.find("b").string[:-1] == "科室":
                department = li.get_text().strip()[4:].replace("\n", " ").strip().replace("\xa0\r", "")
                check_dict["department"] = department
                break
            else:
                check_dict["department"] = None

        for li in li_list:
            if li.find("b").string[:-1] == "空腹检查":
                is_fasting = li.get_text()[5:]
                check_dict["is_fasting"] = is_fasting
                break
            else:
                check_dict["is_fasting"] = None

        for li in li_list:
            if li.find("b").string[:-1] == "禁忌人群":
                taboo = li.get_text()[7:].strip()
                check_dict["taboo"] = taboo
                break
            else:
                check_dict["taboo"] = None

        for li in li_list:
            if li.find("b").string[:-1] == "医院参考价":
                price = li.get_text()[8:].strip().rstrip("查看详细>>")
                check_dict["price"] = price
                break
            else:
                check_dict["price"] = None

        for li in li_list:
            if li.find("b").string[:-1] == "指标解读":
                in1 = li.find("dl", attrs={"class": "s1"}).find("dd").get_text().strip().replace("\n", "").replace(
                    "\u3000", "").replace("\r", "")
                in2 = li.find("dl", attrs={"class": "s2"}).find("dd").get_text().strip().replace("\n", "").replace(
                    "\u3000", "").replace("\r", "")
                check_dict["indicator"] = in1 + in2
                break
            else:
                check_dict["indicator"] = None

        div_list = soup.find_all("div", attrs={"class": "lbox catalogItem"})  # 各种大标题所在div标签

        for div in div_list:
            if div.find("h3").string.lstrip(name) == "注意事项":
                atten = div.find("div", attrs={"class": "text"}).get_text().replace("\u3000", "").replace("\n", "")
                check_dict["atten"] = atten
                break
            else:
                check_dict["atten"] = None

        for div in div_list:
            if div.find("h3").string.lstrip(name) == "检查作用":
                purpose = div.find("div", attrs={"class": "text"}).get_text().replace("\u3000", "").replace("\n", "")
                check_dict["purpose"] = purpose
                break
            else:
                check_dict["purpose"] = None

        for div in div_list:
            if div.find("h3").string.lstrip(name) == "检查过程":
                process = div.find("div", attrs={"class": "text"}).get_text().replace("\u3000", "").replace("\n", "")
                check_dict["process"] = process
                break
            else:
                check_dict["process"] = None

        for li in li_list:  # 相关疾病、外码
            if li.find("b").string[:-1] == "相关疾病":
                disease_list = []
                a_list = li.find_all("a")
                for a in a_list[:-1]:
                    disease_list.append(a.get("href")[19:-1])
                check_dict["disease"] = disease_list
                break
            else:
                check_dict["disease"] = None

        for li in li_list:  # 相关症状、外码
            if li.find("b").string[:-1] == "相关症状":
                symptom_list = []
                a_list = li.find_all("a")
                for a in a_list[:-1]:
                    symptom_list.append(a.get("href")[31:-1])
                check_dict["symptom"] = symptom_list
                break
            else:
                check_dict["symptom"] = None

        check_f.write(str(check_dict))  # txt文件将会保存检查 check实体字典
        check_f.write("\n")
    check_f.close()
