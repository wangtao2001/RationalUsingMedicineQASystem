# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/05/22, Sat

def read_file():
    """读入文件，形成列表，每个列表都是一个实体（字典）"""
    with open(r"../substance/check.txt", 'r', encoding='utf-8') as check_f:
        check_data = [eval(dicts) for dicts in check_f.readlines()]
    with open(r"../substance/department.txt", 'r', encoding='utf-8') as department_f:
        department_data = [{"name": names} for names in department_f.readlines()]
    with open(r"../substance/disease.txt", 'r', encoding='utf-8') as disease_f:
        disease_data = [eval(dicts) for dicts in disease_f.readlines()]
    with open(r"../substance/medical.txt", 'r', encoding='utf-8') as medical_f:
        medical_data = [eval(dicts) for dicts in medical_f.readlines()]
    with open(r"../substance/symptom.txt", 'r', encoding='utf-8') as symptom_f:
        symptom_data = [eval(dicts) for dicts in symptom_f.readlines()]
    return [check_data, department_data, disease_data, medical_data, symptom_data]


def node_extraction():
    """
    抽取所有结点
    即实体文件中不包含属性的部分
    返回所有实体 格式为 {'label': [{node}, {node}, ...], ..}
    """
    substance = ['check', 'department', 'disease', 'medical', 'symptom']
    node_dict = dict()
    for i in range(5):
        node_dict[substance[i]] = []
        for sub in read_file()[i]:
            node = dict((key, value) for key, value in sub.items() if not type(value) == type([]))  # 实体中值是列表的表示关系而不是属性
            node_dict[substance[i]].append(node)
    return node_dict


if __name__ == "__main__":
    print(len(node_extraction()))