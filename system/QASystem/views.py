from django.http import *
from django.views.decorators.csrf import csrf_exempt
from py2neo import Graph
from . import node_names as node

user = "neo4j"
password = "qazplm-55454"

driver = Graph("http://localhost:7474",
               user=user,
               password=password)


@csrf_exempt  # 跳过csrf验证
def get_answer(request: HttpRequest):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        type = request.POST['type']

        if type == '0':  # 问题提交
            question = request.POST['questionOrTitle']
            print('question: ' + question)
            # 问答接口
            answer = "竹叶配伍的美容方剂有：清凉爽身浴方、体臭方、常用蜡脂方"
            center_node_name = "竹叶"
            center_node_type = "中药"
            answer_node_names = ["清凉爽身浴方", "体臭方", "常用蜡脂方"]
            answer_node_type = "美容方剂"
            # 还原所有结点的大小
            driver.run('MATCH (n) REMOVE n.point')
            # 将答案结点变大
            if answer_node_names:
                for name in answer_node_names:
                    driver.run(
                        f"MATCH (n:`{answer_node_type}`) WHERE n.{node.names[answer_node_type]} = '{name}' SET n.point=3")
            # 获取查询Cypther 即绘制中心结点的所有关系
            cypher = f"MATCH (n:`{center_node_type}`)-[r]-(m) WHERE n.{node.names[center_node_type]} = '{center_node_name}' RETURN n,r,m LIMIT 100"
            tip = f"{center_node_name}结点的查询结果与相关关系"

        elif type == '1':  # 以下为快捷导航栏提交
            title = request.POST['questionOrTitle']
            cypher = f"MATCH (n:`department`)-[r]-(m) WHERE n.name = '{title}' RETURN n,r,m LIMIT 50"
            answer = f"{title}"
            tip = f"与{title}相关的症状、检查或疾病"

        elif type == '2':  # 辨证法 ## 注意辨证
            title = request.POST['questionOrTitle']
            cypher = f"MATCH (m)-[r]-(n:`辨证法`) WHERE n.辨证法名称 = '{title}' RETURN n,r,m LIMIT 50"
            answer = f'''{title}：{driver.run("match(n:`辨证法`) where n.辨证法名称 = '八纲辨证' return n.辨证法含义").data()[0]['n.辨证法含义']}'''
            tip = f"与{title}相关的证候"

        elif type == '3':  # 中药分类
            title = request.POST['questionOrTitle']
            cypher = f"MATCH (n:`中药分类`)-[r]-(m) WHERE n.中药分类名称 = '{title}' RETURN n,r,m LIMIT 50"
            li = [i['n']['中药名称'] for i in driver.run(
                "MATCH(n:`中药`)-[]->(m:`中药分类`) WHERE m.中药分类名称 = '驱虫药' RETURN n LIMIT 9").data()]
            answer = f"与{title}相关的中药有：{'、'.join(li)} 等"
            tip = f"与{title}相关的中药"

        else:
            pass

        # 向前端返回数据
        return JsonResponse({
            'answer': answer,  # 问题答案
            'cypher': cypher,  # 图谱渲染Cypher
            'tip': tip  # 图谱底部提示
        })
    else:
        pass
