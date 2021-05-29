# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/05/22, Sat

substance = ['check', 'department', 'disease', 'medical', 'symptom']


def read_file():
    """读入文件，形成列表，每个列表都是一个实体（字典）"""
    with open(r"../substance/check.txt", 'r', encoding='utf-8') as check_f:
        check_data = [eval(dicts) for dicts in check_f.readlines()]
    with open(r"../substance/department.txt", 'r', encoding='utf-8') as department_f:
        department_data = [eval(dicts) for dicts in department_f.readlines()]
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
    """
    node_dict = dict()
    for i in range(5):
        node_dict[substance[i]] = []
        for sub in read_file()[i]:
            node = dict((key, value) for key, value in sub.items() if not type(value) == type([]))
            node_dict[substance[i]].append(node)
    return node_dict


def relationship_extraction():
    """
    关系提取
    返回实体中的关系部分
    """
    relationship_dict = dict()
    for i in range(5):
        if i != 1 and i != 3:  # 疾病、科室没有外指向
            relationship_dict[substance[i]] = []
            for sub in read_file()[i]:
                relationship = dict((key, value) for key, value in sub.items() if type(value) == type([]))
                relationship = {sub['id']: relationship}
                relationship_dict[substance[i]].append(relationship)
        else:
            pass
    return relationship_dict


if __name__ == "__main__":
    pass
