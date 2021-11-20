from django.http import *
from django.views.decorators.csrf import csrf_exempt
from py2neo import Graph


@csrf_exempt
def get_answer(request: HttpRequest):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        question = request.POST['question']
        print(question)
        # 问答接口
        answer = "中风通常的使用的药品包括：低分子肝素；华法林；依达拉奉；阿司匹林；胞二磷胆；氯吡格雷"
        center_node_name = "竹叶"
        center_node_type = "中药"
        answer_node_names = ["清凉爽身浴方", "体臭方", "常用蜡脂肪方"]
        answer_node_type = "美容方剂"
        # 返回数据
        # 还原所有结点的大小
        # 将答案结点变大
        return JsonResponse({
            'answer': answer,
            'center_node_name': center_node_name,
            'center_node_type': center_node_type,
            'answer_node_names': answer_node_names,
            'answer_node_type': answer_node_type
        })
    else:
        pass
