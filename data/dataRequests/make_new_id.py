# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author: wangtao
# @create on: 21/08/14, Sat

"""
为实体重新编制新id
设计数据库第一次永远要设计好主键，不要给自己挖坑！！
"""

sub_path = '../substance/'

with open(sub_path + "check.txt", 'r', encoding='utf-8') as check_f:
    check_data = [eval(dicts) for dicts in check_f.readlines()]
with open(sub_path + "department.txt", 'r', encoding='utf-8') as department_f:
    department_data = [eval(dicts) for dicts in department_f.readlines()]
with open(sub_path + "disease.txt", 'r', encoding='utf-8') as disease_f:
    disease_data = [eval(dicts) for dicts in disease_f.readlines()]
with open(sub_path + "medical.txt", 'r', encoding='utf-8') as medical_f:
    medical_data = [eval(dicts) for dicts in medical_f.readlines()]
with open(sub_path + "symptom.txt", 'r', encoding='utf-8') as symptom_f:
    symptom_data = [eval(dicts) for dicts in symptom_f.readlines()]

# 修改初始id值
for i in range(len(check_data)):
    check_data[i]['_id'] = 'C' + str(i).zfill(5)

for i in range(len(department_data)):
    department_data[i]['_id'] = 'E' + str(i).zfill(3)

for i in range(len(disease_data)):
    disease_data[i]['_id'] = 'I' + str(i).zfill(5)

for i in range(len(medical_data)):
    medical_data[i]['_id'] = 'M' + str(i).zfill(5)

for i in range(len(symptom_data)):
    symptom_data[i]['_id'] = 'S' + str(i).zfill(5)


# 修改外键
def func(a: str, b: str):  # check symptom
    for i in range(len(eval(f'{a}_data'))):
        b_li = eval(f'{a}_data')[i][b]
        new_b = []
        if b_li is not None:
            for b_item in b_li:
                for b_dict in eval(f'{b}_data'):
                    if b_dict['id'] == b_item:
                        new_b.append(b_dict['_id'])
                        break
        eval(f'{a}_data')[i][b] = new_b
    print(a + " " + b)


func('disease', 'disease')
func('disease', 'medical')
func('disease', 'symptom')
func('disease', 'check')
func('check', 'disease')
func('check', 'symptom')
func('symptom', 'disease')
func('symptom', 'check')
func('disease', 'department')
func('symptom', 'department')
func('check', 'department')

f = open('../substance/check.txt', 'w', encoding='utf-8')
for i in range(len(check_data)):
    del check_data[i]['id']
    f.write(str(check_data[i]) + '\n')
f.close()

f = open('../substance/department.txt', 'w', encoding='utf-8')
for i in range(len(department_data)):
    del department_data[i]['id']
    f.write(str(department_data[i]) + '\n')
f.close()

f = open('../substance/disease.txt', 'w', encoding='utf-8')
for i in range(len(disease_data)):
    del disease_data[i]['id']
    f.write(str(disease_data[i]) + '\n')
f.close()

f = open('../substance/medical.txt', 'w', encoding='utf-8')
for i in range(len(medical_data)):
    del medical_data[i]['id']
    f.write(str(medical_data[i]) + '\n')
f.close()

f = open('../substance/symptom.txt', 'w', encoding='utf-8')
for i in range(len(symptom_data)):
    del symptom_data[i]['id']
    f.write(str(symptom_data[i]) + '\n')
f.close()
