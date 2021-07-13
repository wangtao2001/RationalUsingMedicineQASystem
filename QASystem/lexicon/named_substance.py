# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/07/13, Tue

from dataSaving.dataFormatting import *
import re

if __name__ == '__main__':
    with open('./lexicon.txt', 'w', encoding='utf-8') as sub_f:
        node_dict = node_extraction()

        for i in range(5):
            for item in node_dict[substance[i]]:
                for key in list(item.keys()):
                    if re.match('.*name$', key):
                        if item[key] is not None:
                            sub_f.write(item[key] + '\n')
