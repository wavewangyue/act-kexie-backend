#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 16:03
# @Author  : WangFei
# @Des     : 
import json
from django.http import HttpResponse
import urllib
import codecs
import sys

xuehui_list_data=json.load(codecs.open(sys.path[0]+u'/static/dxs_data/dxs/xuehui_list_data.json',"r",encoding="utf-8"))
china_map_data=json.load(codecs.open(sys.path[0]+u'/static/dxs_data/dxs/china_map_data.json',"r",encoding="utf-8"))
world_map_data=json.load(codecs.open(sys.path[0]+u'/static/dxs_data/dxs/world_map_data.json',"r",encoding="utf-8"))
s_e_data=json.load(codecs.open(sys.path[0]+u'/static/dxs_data/dxs/s_e_data_190318.json',"r",encoding="utf-8"))


def dxs_url_demo(request):
    result=["demo"]
    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_xuehui_list_data(request):
    result=xuehui_list_data
    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_china_map_data(request):
    result=china_map_data
    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_world_map_data(request):
    result=world_map_data
    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_s_e_data(request):
    result=s_e_data
    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_redian_data(request):
    subject_data = {
        "计算机技术": {
            "机器学习": 30749,
            "深度学习": 13230,
            "网络安全": 11486,
            "云计算": 8548,
            "物联网": 6556
        },
        "电信技术": {
            "5G": 23468,
            "移动通信": 18497,
            "无线网络": 14962,
            "4G": 11351,
            "可信计算": 8842
        },
        "半导体技术": {
            "集成电路": 46468,
            "传感器": 24344,
            "微电子": 13260,
            "半导体材料": 7147,
            "半导体器件": 4601

        }
    }

    nodes_relations = {
        "nodes": [
            {
                "id": 0,
                "name": "卷积神经网络",
                "value": 23,
                "category": "卷积神经网络"
            },
            {
                "id": 1,
                "name": "深度学习",
                "value": 25,
                "category": "深度学习"
            },
            {
                "id": 2,
                "name": "神经网络",
                "value": 17,
                "category": "神经网络"
            },
            {
                "id": 3,
                "name": "机器学习",
                "value": 33,
                "category": "机器学习"
            },
            {
                "id": 4,
                "name": "遗传算法",
                "value": 18,
                "category": "遗传算法"
            },
            {
                "id": 5,
                "name": "特征提取",
                "value": 17,
                "category": "特征提取"
            },
            {
                "id": 6,
                "name": "人工智能",
                "value": 20,
                "category": "人工智能"
            },
            {
                "id": 7,
                "name": "文本分类",
                "value": 12,
                "category": "文本分类"
            },
            {
                "id": 8,
                "name": "云计算",
                "value": 19,
                "category": "云计算"
            },
            {
                "id": 9,
                "name": "监督学习",
                "value": 18,
                "category": "监督学习"
            }
        ],
        "links": [
            {
                "source": 0,
                "target": 0,
                "count": 345
            },
            {
                "source": 0,
                "target": 1,
                "count": 118
            },
            {
                "source": 0,
                "target": 2,
                "count": 13
            },
            {
                "source": 1,
                "target": 1,
                "count": 457
            },
            {
                "source": 1,
                "target": 2,
                "count": 36
            },
            {
                "source": 1,
                "target": 3,
                "count": 31
            },
            {
                "source": 1,
                "target": 9,
                "count": 23
            },
            {
                "source": 2,
                "target": 4,
                "count": 323
            },
            {
                "source": 2,
                "target": 5,
                "count": 65
            },
            {
                "source": 2,
                "target": 6,
                "count": 8
            },
            {
                "source": 3,
                "target": 3,
                "count": 3069
            },
            {
                "source": 3,
                "target": 4,
                "count": 71
            },
            {
                "source": 3,
                "target": 5,
                "count": 198
            },
            {
                "source": 3,
                "target": 6,
                "count": 5
            },
            {
                "source": 3,
                "target": 7,
                "count": 159
            },
            {
                "source": 3,
                "target": 9,
                "count": 15
            },
            {
                "source": 4,
                "target": 4,
                "count": 4314
            },
            {
                "source": 4,
                "target": 5,
                "count": 23
            },
            {
                "source": 5,
                "target": 5,
                "count": 2501
            },
            {
                "source": 5,
                "target": 7,
                "count": 32
            },
            {
                "source": 6,
                "target": 7,
                "count": 13
            },
            {
                "source": 6,
                "target": 8,
                "count": 55
            },
            {
                "source": 6,
                "target": 9,
                "count": 21
            }
        ]
    }
    nodes_relations2 = {
        "nodes": [
            {
                "id": 0,
                "name": "5G",
                "value": 23,
                "category": "5G"
            },
            {
                "id": 1,
                "name": "无线网络",
                "value": 25,
                "category": "无线网络"
            },
            {
                "id": 2,
                "name": "4G",
                "value": 17,
                "category": "4G"
            },
            {
                "id": 3,
                "name": "LTE",
                "value": 33,
                "category": "LTE"
            },
            {
                "id": 4,
                "name": "软件定义网络",
                "value": 18,
                "category": "软件定义网络"
            },
            {
                "id": 5,
                "name": "网络功能虚拟化",
                "value": 17,
                "category": "网络功能虚拟化"
            },
            {
                "id": 6,
                "name": "移动通信",
                "value": 20,
                "category": "移动通信"
            },
            {
                "id": 7,
                "name": "cdma网络",
                "value": 12,
                "category": "cdma网络"
            },
            {
                "id": 8,
                "name": "移动网络",
                "value": 19,
                "category": "移动网络"
            },
            {
                "id": 9,
                "name": "网络接入",
                "value": 18,
                "category": "网络接入"
            }
        ],
        "links": [
            {
                "source": 0,
                "target": 0,
                "count": 345
            },
            {
                "source": 0,
                "target": 1,
                "count": 118
            },
            {
                "source": 0,
                "target": 2,
                "count": 13
            },
            {
                "source": 1,
                "target": 1,
                "count": 457
            },
            {
                "source": 1,
                "target": 2,
                "count": 36
            },
            {
                "source": 1,
                "target": 3,
                "count": 31
            },
            {
                "source": 1,
                "target": 9,
                "count": 23
            },
            {
                "source": 2,
                "target": 4,
                "count": 323
            },
            {
                "source": 2,
                "target": 5,
                "count": 65
            },
            {
                "source": 2,
                "target": 6,
                "count": 8
            },
            {
                "source": 3,
                "target": 3,
                "count": 3069
            },
            {
                "source": 3,
                "target": 4,
                "count": 71
            },
            {
                "source": 3,
                "target": 5,
                "count": 198
            },
            {
                "source": 3,
                "target": 6,
                "count": 5
            },
            {
                "source": 3,
                "target": 7,
                "count": 159
            },
            {
                "source": 3,
                "target": 9,
                "count": 15
            },
            {
                "source": 4,
                "target": 4,
                "count": 4314
            },
            {
                "source": 4,
                "target": 5,
                "count": 23
            },
            {
                "source": 5,
                "target": 5,
                "count": 2501
            },
            {
                "source": 5,
                "target": 7,
                "count": 32
            },
            {
                "source": 6,
                "target": 7,
                "count": 13
            },
            {
                "source": 6,
                "target": 8,
                "count": 55
            },
            {
                "source": 6,
                "target": 9,
                "count": 21
            }
        ]
    }
    nodes_relations3 = {
        "nodes": [
            {
                "id": 0,
                "name": "集成电路",
                "value": 23,
                "category": "集成电路"
            },
            {
                "id": 1,
                "name": "微电子",
                "value": 25,
                "category": "微电子"
            },
            {
                "id": 2,
                "name": "芯片",
                "value": 17,
                "category": "芯片"
            },
            {
                "id": 3,
                "name": "驱动电路",
                "value": 33,
                "category": "驱动电路"
            },
            {
                "id": 4,
                "name": "微处理器",
                "value": 18,
                "category": "微处理器"
            },
            {
                "id": 5,
                "name": "传感器",
                "value": 17,
                "category": "传感器"
            },
            {
                "id": 6,
                "name": "嵌入式处理器",
                "value": 20,
                "category": "嵌入式处理器"
            },
            {
                "id": 7,
                "name": "电子技术",
                "value": 12,
                "category": "电子技术"
            },
            {
                "id": 8,
                "name": "微电子器件",
                "value": 19,
                "category": "微电子器件"
            },
            {
                "id": 9,
                "name": "微系统",
                "value": 18,
                "category": "微系统"
            }
        ],
        "links": [
            {
                "source": 0,
                "target": 0,
                "count": 345
            },
            {
                "source": 0,
                "target": 1,
                "count": 118
            },
            {
                "source": 0,
                "target": 2,
                "count": 13
            },
            {
                "source": 1,
                "target": 1,
                "count": 457
            },
            {
                "source": 1,
                "target": 2,
                "count": 36
            },
            {
                "source": 1,
                "target": 3,
                "count": 31
            },
            {
                "source": 1,
                "target": 9,
                "count": 23
            },
            {
                "source": 2,
                "target": 4,
                "count": 323
            },
            {
                "source": 2,
                "target": 5,
                "count": 65
            },
            {
                "source": 2,
                "target": 6,
                "count": 8
            },
            {
                "source": 3,
                "target": 3,
                "count": 3069
            },
            {
                "source": 3,
                "target": 4,
                "count": 71
            },
            {
                "source": 3,
                "target": 5,
                "count": 198
            },
            {
                "source": 3,
                "target": 6,
                "count": 5
            },
            {
                "source": 3,
                "target": 7,
                "count": 159
            },
            {
                "source": 3,
                "target": 9,
                "count": 15
            },
            {
                "source": 4,
                "target": 4,
                "count": 4314
            },
            {
                "source": 4,
                "target": 5,
                "count": 23
            },
            {
                "source": 5,
                "target": 5,
                "count": 2501
            },
            {
                "source": 5,
                "target": 7,
                "count": 32
            },
            {
                "source": 6,
                "target": 7,
                "count": 13
            },
            {
                "source": 6,
                "target": 8,
                "count": 55
            },
            {
                "source": 6,
                "target": 9,
                "count": 21
            }
        ]
    }
    nodes_relation_all = {}
    nodes_relation_all["计算机技术"] = nodes_relations
    nodes_relation_all["电信技术"] = nodes_relations2
    nodes_relation_all["半导体技术"] = nodes_relations3

    result={"subject_data":subject_data,"nodes_relation_all":nodes_relation_all}
    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_sci_ei_data(request):
    sci_ei = [{"name":"SCI收录中国期刊数","type":"bar","data":[104,108,115,128,134,135,139,142,148,162,173]},{"name":"EI收录中国期刊数","type":"bar","data":[174,197,217,210,211,207,216,216,216,215,221]}]
    result = sci_ei
    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_huodong_data(request):
    huodong_data=['34542场\n学术会议','610万人\n参会人数','109.4万篇\n交流论文','10121场\n高端前沿会议','11554场\n综合交叉会议','12867场\n学术服务会议']
    result=huodong_data
    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response