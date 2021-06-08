# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/06/08, Mon

if __name__ == "__main__":
    medical_interaction_list = list()

    with open('../substance/medical.txt', 'r', encoding='utf-8') as f:
        dicts = [eval(_dict) for _dict in f.readlines()]
        for _dict in dicts:
            if _dict['medical'] is None:
                continue
            t = {key: value for key, value in _dict.items() if key == 'id' or key == 'medical'}  # 只收集药物id与药物相互作用字段
            medical_interaction_list.append(t)