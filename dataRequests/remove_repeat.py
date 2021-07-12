# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/04/06, Mon

class RemoveRepeat:
    def __init__(self, file, name):
        li = [i.strip() for i in file.readlines()]  # 每个元素都是字典
        print(f"去重前：{len(li)}")
        li = list(set(li))
        print(f"去重后：{len(li)}")
        with open(rf".\data\{name}.txt", "w", encoding='utf-8') as f:
            for i in li:
                f.write(i)
                f.write("\n")


if __name__ == "__main__":
    with open(r".\data\medical_url_repeat.txt", "r", encoding='utf-8') as file:
        RemoveRepeat(file, "medical_url")
    with open(r".\data\check_url_repeat.txt", "r", encoding='utf-8') as file:
        RemoveRepeat(file, "check_url")
    with open(r".\data\symptom_url_repeat.txt", "r", encoding='utf-8') as file:
        RemoveRepeat(file, "symptom_url")
