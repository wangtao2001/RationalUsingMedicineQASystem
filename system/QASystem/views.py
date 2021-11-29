from django.http import *
from django.views.decorators.csrf import csrf_exempt
from py2neo import Graph
from . import node_names as node

driver = Graph("http://localhost:7474",
               user="neo4j",
               password="qazplm-55454")


@csrf_exempt
def get_answer(request: HttpRequest):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        type = request.POST['type']

        if type == '0':  # 问题提交
            question = request.POST['questionOrTitle']
            print('question: '+question)

            # 问答接口
            answer = "竹叶配伍的美容方剂有：清凉爽身浴方、体臭方、常用蜡脂肪方"
            center_node_name = "竹叶"
            center_node_type = "中药"
            answer_node_names = ["清凉爽身浴方", "体臭方", "常用蜡脂肪方"]
            answer_node_type = "美容方剂"

            # 还原所有结点的大小
            driver.run('MATCH (n) REMOVE n.point')

            # 将答案结点变大
            if answer_node_names:
                for name in answer_node_names:
                    driver.run(
                        f"MATCH (n:`{answer_node_type}`) WHERE n.{node.names[answer_node_type]} = '{name}' SET n.point=3")

            # 获取查询Cypther 即绘制中心结点的所有关系
            cypher = f"MATCH (n:`{center_node_type}`)-[r]-(m) WHERE n.{node.names[center_node_type]} = '{center_node_name}' RETURN n,r,m"

        elif type == '1':  # 以下为快捷导航栏提交
            title = request.POST['questionOrTitle']
            cypher = f"MATCH (n:`科室`)-[r]=(m) WHERE n.name == {title} RETURN n,r,m"

        elif type == '2':
            pass
        elif type == '3':
            pass
        else:
            pass

        # 向前端返回数据
        return JsonResponse({
            'answer': answer,
            'cypher': cypher
        })
    else:
        pass
