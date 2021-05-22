# !/usr/bin/env python3
# -*-coding: utf-8-*-
# @author:  wangtao
# @data: 21/05/22, Sat

from dataFormatting import *
from dataToNeo4j import *

neo = DataToNeo4j()
neo.create_node(node_extraction())