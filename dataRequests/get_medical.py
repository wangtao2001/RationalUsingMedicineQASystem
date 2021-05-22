# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author: wangtao
# @create on: 21/04/06, Mon

import requests
from bs4 import BeautifulSoup

start_url = "https://ybk.39.net/"
headers = {r"user-agent": "Mozilla\5.0"}

def get_attr(attr_name: str, attr: str):
    global medical_dict  # 全局字典
    global li_list  # 全局 li_list
    for li in li_list:
        if li.find("p", attrs={"class": "drug-explain-tit"}).string[1:-1] == attr_name:
            value = li.find("p", attrs={"class": "drug-explain-txt"}).text.strip()
            # 文字中可能含有p和br标签
            medical_dict[attr] = value.lstrip("<p>").rstrip("</p>").replace("<br />", "").replace("\n", " ")
            break
        else:
            medical_dict[attr] = None


if __name__ == "__main__":

    with open(r"../data/medical_url.txt", 'r', encoding='utf-8') as medical_url_f:
        medical_url_list_tp = [eval(url) for url in medical_url_f.readlines()]  # 每个元素都是字典
    medical_url_list = [di[key] for di in medical_url_list_tp for key in di.keys()]  # 所有药品url的列表

    medical_f = open(r"../substance/medical.txt", 'a', encoding='utf-8')  # medical实体文件

    count = 0  # 计数器

    for url in medical_url_list[count:]:  # 6696条数据 无重复 index = 0:6696
        count += 1
        print(count)

        medical_dict = dict()
        url += "manual/"

        r = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(r.content, 'html.parser')

        medical_dict["id"] = url[18:-8]  # 写入唯一标识符
        # icon1：处方、icon2：国家医保目录（甲类）、icon3：国家医保目录（乙类）、icon4：外用药物、icon5：国家基本药物目录（2012）
        try:
            medical_dict['is_recipe'] = soup.find("i", attrs={"class": "drug-layout-r-icon1"}).string  # 写入是否处方
        except:
            medical_dict['is_recipe'] = None
        try:
            icon2 = soup.find("i", attrs={"class": "drug-layout-r-icon2"}) # 甲类
            if icon2 is None:
                raise ValueError
        except:
            try:
                icon3 = soup.find("i", attrs={"class": "drug-layout-r-icon3"}) # 乙类
                if icon3 is None:
                    raise ValueError
            except:
                medical_dict["insurance"] = None
            else:
                medical_dict["insurance"] = icon3.string
        else:
            medical_dict["insurance"] = icon2.string

        ul = soup.find("ul", attrs={"class": "drug-explain"})
        li_list = ul.find_all("li",recursive=False)  # 在子孙节点中可能也含有li

        # 药品名称 name（通用名称、商品名称、英文名称、汉语拼音）
        for li in li_list:
            if li.find("p", attrs={"class": "drug-explain-tit"}).string[1:-1] == "药品名称":
                name_list = [s.strip() for s in
                             li.find("p", attrs={"class": "drug-explain-txt"}).get_text().strip().split(
                                 '\n')]  # 包含各种name的列表
                for name in name_list:
                    if name[:4] == "通用名称":
                        medical_dict["name"] = name.split("：")[1]
                    elif name[:4] == "商品名称":
                        medical_dict["product_name"] = name.split("：")[1]
                    elif name[:4] == "英文名称":
                        medical_dict["en_name"] = name.split("：")[1]
                    elif name[:4] == "汉语拼音":
                        medical_dict["pinyin_name"] = name.split("：")[1]
                    else:
                        pass
                break
            else:
                medical_dict.update({"name": None, "product_name": None, "en_name": None, "pinyin_name": None})

        get_attr("成份", "ingredient")
        get_attr("性状", "character")
        get_attr("适应症", "disease")  # 有的药品写作适应症、有的写作功能主治
        get_attr("功能主治", "function")
        get_attr("用法用量", "usage")
        get_attr("不良反应", "adverse_reaction")
        get_attr("禁忌", "taboo")
        get_attr("注意事项", "attention")

        # 儿童、妊娠、老人注意事项
        for li in li_list:
            if li.find("p", attrs={"class": "drug-explain-tit"}).string[1:-1] == "特殊人群用药":
                atten_list = [s.strip() for s in
                              li.find("p", attrs={"class": "drug-explain-txt"}).get_text().strip().split("\n")]
                try:
                    medical_dict["child_atten"] = atten_list[2]
                except IndexError:
                    medical_dict["child_atten"] = None
                try:
                    medical_dict["pregnancy_atten"] = atten_list[6]
                except IndexError:
                    medical_dict["pregnancy_atten"] = None
                try:
                    medical_dict["older_atten"] = atten_list[10]
                except IndexError:
                    medical_dict["older_atten"] = None
                break
            else:
                medical_dict.update({"child_atten": None, "pregnancy_atten": None, "older_atten": None})

        get_attr("药物相互作用", "medical")
        get_attr("药理作用", "pharmacology")
        get_attr("贮藏", "depot")
        get_attr("规格", "size")
        get_attr("包装规格", "package_size")
        get_attr("有效期", "data")
        get_attr("批准文号", "number")

        # 生产企业
        for li in li_list:
            if li.find("p", attrs={"class": "drug-explain-tit"}).string[1:-1] == "生产企业":
                p2 = li.find("p", attrs={"class": "drug-explain-txt"})
                medical_dict["company"] = " ".join(p2.get_text().strip().split()) + "。"

        medical_f.write(str(medical_dict))  # txt文件将会保存药品 medical实体字典
        medical_f.write("\n")
    medical_f.close()
