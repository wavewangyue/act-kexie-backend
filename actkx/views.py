import json
from django.http import HttpResponse
import urllib
import time
import hashlib
import sys

def get_online_user_num(request):

    timestamp = str(time.time()).split(".")[0]

    str1 = "appid=kepu_sciwisdom&path=/sciwisdom/getuseronline&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"
    sn1 = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn1 = hashlib.md5(sn1.encode("utf-8")).hexdigest()
    url1 = "https://open-api.kepuchina.cn/sciwisdom/getuseronline?appid=kepu_sciwisdom&timestamp="+timestamp+"&sn="+sn1
    
    str2 = "appid=kejie_sciwisdom&path=/sciwisdom/getuseronline&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn2 = hashlib.md5(str2.encode("utf-8")).hexdigest()
    sn2 = hashlib.md5(sn2.encode("utf-8")).hexdigest()
    url2 = "https://openapi.scimall.org.cn/sciwisdom/getuseronline?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn2

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result1 = json.loads(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    result2 = json.loads(str(urllib.request.urlopen(url2, timeout=10).read(),encoding="utf-8"))

    num = result1["data"]["num"] + result2["data"]["num"] + 375
    #num=1
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_online_user_num_three(request):
    timestamp = str(time.time()).split(".")[0]

    str1 = "appid=kepu_sciwisdom&path=/sciwisdom/getuseronline&timestamp=" + timestamp + "&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"
    sn1 = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn1 = hashlib.md5(sn1.encode("utf-8")).hexdigest()
    url1 = "https://open-api.kepuchina.cn/sciwisdom/getuseronline?appid=kepu_sciwisdom&timestamp=" + timestamp + "&sn=" + sn1

    str2 = "appid=kejie_sciwisdom&path=/sciwisdom/getuseronline&timestamp=" + timestamp + "&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn2 = hashlib.md5(str2.encode("utf-8")).hexdigest()
    sn2 = hashlib.md5(sn2.encode("utf-8")).hexdigest()
    url2 = "https://openapi.scimall.org.cn/sciwisdom/getuseronline?appid=kejie_sciwisdom&timestamp=" + timestamp + "&sn=" + sn2

    # print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))

    result1 = json.loads(str(urllib.request.urlopen(url1, timeout=10).read(), encoding="utf-8"))
    result2 = json.loads(str(urllib.request.urlopen(url2, timeout=10).read(), encoding="utf-8"))

    num = result1["data"]["num"] + result2["data"]["num"] + 375
    result={"kepu":result1["data"]["num"],"kejie":result2["data"]["num"]}
    # num=1
    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_top_words(request):

    timestamp = str(time.time()).split(".")[0]

    str1 = "appid=kepu_sciwisdom&path=/sciwisdom/top20&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://open-api.kepuchina.cn/sciwisdom/top20?appid=kepu_sciwisdom&timestamp="+timestamp+"&sn="+sn
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response




def get_per(request):

    province_code = request.GET.get("province_code", "150000000000")
    ch_id = request.GET.get("ch_id", "AT201604301608271001")

    timestamp = str(time.time()).split(".")[0]

    str1 = "appid=kepu_sciwisdom&ch_id="+ch_id+"&page=1&path=/Articlecount/getSciencerCount&province_code="+province_code+"&size=20&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://open-api.kepuchina.cn/Articlecount/getSciencerCount?appid=kepu_sciwisdom&timestamp="+timestamp+"&province_code="+province_code+"&ch_id="+ch_id+"&page=1&size=20"+"&sn="+sn

    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))
    
    result = {"list":result["data"]["list"],"total":result["data"]["total"]}

    #result = {"list":[{"sciencer_name":province_code,"province_name":ch_id,"experience":ch_id}]*20, "total":99}

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response





def get_org(request):

    province_code = request.GET.get("province_code", "150000000000")
    ch_id = request.GET.get("ch_id", "AT201604301608271001")

    timestamp = str(time.time()).split(".")[0]

    str1 = "appid=kepu_sciwisdom&ch_id="+ch_id+"&page=1&path=/Articlecount/getSourceCount&province_code="+province_code+"&size=20&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"  
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://open-api.kepuchina.cn/Articlecount/getSourceCount?appid=kepu_sciwisdom&timestamp="+timestamp+"&province_code="+province_code+"&ch_id="+ch_id+"&page=1&size=20"+"&sn="+sn

    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))
    
    result = {"list":result["data"]["list"],"total":result["data"]["total"]}

    #result = {"list":[{"article_source":"新华网","province_name":"北京","num":"1100"}]*10, "total":99}

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response



def get_art(request):

    province_code = request.GET.get("province_code", "150000000000")
    ch_id = request.GET.get("ch_id", "AT201604301608271001")

    timestamp = str(time.time()).split(".")[0]

    str1 = "appid=kepu_sciwisdom&ch_id="+ch_id+"&page=1&path=/Articlecount/getArticleCount&province_code="+province_code+"&size=20&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://open-api.kepuchina.cn/Articlecount/getArticleCount?appid=kepu_sciwisdom&timestamp="+timestamp+"&province_code="+province_code+"&ch_id="+ch_id+"&page=1&size=20"+"&sn="+sn

    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    result = {"list":result["data"]["list"],"total":result["data"]["total"]}

    #result = {"list":[{"ar_name":province_code,"province_name":"北京","article_source":"科普中国","hits":"1000"}]*10,"total":99}

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_map(type1,type2,type3): #type1 场馆级别 type2 单位性质 type3 隶属关系
    file1 = open(sys.path[0]+u'/static/museum_data/2017年全国科技馆调查统计表-192家达标科技馆.json', "r",encoding="utf-8")
    fileJson1 = json.load(file1)
    map_data = {}
    result_data = []
    for item in fileJson1:
        if type1 != u'全部' and type1 == item[u'场馆级别']:

            if type2 != u'全部'and type2 == item[u'单位性质']:
                if type3 != u'全部' and type3 == item[u'隶属关系']:
                    province = item[u'省份']
                    if province not in map_data:
                        map_data[province] = 1
                    else:
                        map_data[province] += 1
                elif type3 == u'全部':
                    province = item[u'省份']
                    if province not in map_data:
                        map_data[province] = 1
                    else:
                        map_data[province] += 1
            elif type2 == u'全部':
                if type3 != u'全部' and type3 == item[u'隶属关系']:
                    province = item[u'省份']
                    if province not in map_data:
                        map_data[province] = 1
                    else:
                        map_data[province] += 1
                elif type3 == u'全部':
                    province = item[u'省份']
                    if province not in map_data:
                        map_data[province] = 1
                    else:
                        map_data[province] += 1
        elif type1 == u'全部':
            print (item['名称'])
            if type2 != u'全部'and type2 == item[u'单位性质']:
                if type3 != u'全部' and type3 == item[u'隶属关系']:
                    province = item[u'省份']
                    if province not in map_data:
                        map_data[province] = 1
                    else:
                        map_data[province] += 1
                elif type3 == u'全部':
                    province = item[u'省份']
                    if province not in map_data:
                        map_data[province] = 1
                    else:
                        map_data[province] += 1
            elif type2 == u'全部':
                if type3 != u'全部' and type3 == item[u'隶属关系']:
                    province = item[u'省份']
                    if province not in map_data:
                        map_data[province] = 1
                    else:
                        map_data[province] += 1
                elif type3 == u'全部':
                    province = item[u'省份']
                    if province not in map_data:
                        map_data[province] = 1
                    else:
                        map_data[province] += 1


    for key in map_data:
        row_data_dict = {}
        row_data_dict['name'] = key
        row_data_dict['value'] = map_data[key]
        result_data.append(row_data_dict)

    return result_data

def get_museum_map(request):
    type1 = request.GET.get("type1", "全部")
    type2 = request.GET.get("type2", "全部")
    type3 = request.GET.get("type3", "全部")

    data = get_map(type1, type2, type3)  # type1 场馆级别 type2 单位性质 type3 隶属关系
    result = {"list": data, "total": 1}

    # result = {"list":[{"ar_name":province_code,"province_name":"北京","article_source":"科普中国","hits":"1000"}]*10,"total":99}

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_list(province,type1,type2,type3): #type1 场馆级别 type2 单位性质 type3 隶属关系
    file1 = open(sys.path[0] + u'/static/museum_data/2017年全国科技馆调查统计表-192家达标科技馆.json', "r", encoding="utf-8")
    fileJson1 = json.load(file1)
    result_data = []
    for item in fileJson1:
        if type1 != u'全部' and type1 == item[u'场馆级别']:

            if type2 != u'全部' and type2 == item[u'单位性质']:
                if type3 != u'全部' and type3 == item[u'隶属关系']:
                    if province == u'全部':
                        result_data.append(item)
                    elif province == item[u'省份']:
                        result_data.append(item)
                elif type3 == u'全部':
                    if province == u'全部':
                        result_data.append(item)
                    elif province == item[u'省份']:
                        result_data.append(item)
            elif type2 == u'全部':
                if type3 != u'全部' and type3 == item[u'隶属关系']:
                    if province == u'全部':
                        result_data.append(item)
                    elif province == item[u'省份']:
                        result_data.append(item)
                elif type3 == u'全部':
                    if province == u'全部':
                        result_data.append(item)
                    elif province == item[u'省份']:
                        result_data.append(item)
        elif type1 == u'全部':
            if type2 != u'全部' and type2 == item[u'单位性质']:
                if type3 != u'全部' and type3 == item[u'隶属关系']:
                    if province == u'全部':
                        result_data.append(item)
                    elif province == item[u'省份']:
                        result_data.append(item)
                elif type3 == u'全部':
                    if province == u'全部':
                        result_data.append(item)
                    elif province == item[u'省份']:
                        result_data.append(item)
            elif type2 == u'全部':
                if type3 != u'全部' and type3 == item[u'隶属关系']:
                    if province == u'全部':
                        result_data.append(item)
                    elif province == item[u'省份']:
                        result_data.append(item)
                elif type3 == u'全部':
                    if province == u'全部':
                        result_data.append(item)
                    elif province == item[u'省份']:
                        result_data.append(item)
    final_data = []
    for item in result_data:
        row_data_dict = {}
        row_data_dict[u'名称'] = item[u'名称']
        row_data_dict[u'省份'] = item[u'省份']
        row_data_dict[u'场馆级别'] = item[u'场馆级别']
        if u'单位性质' in item:
            row_data_dict[u'单位性质'] = item[u'单位性质']
        else:
            row_data_dict[u'单位性质'] = u"暂缺"
        if u'隶属关系' in item:
            row_data_dict[u'隶属关系'] = item[u'隶属关系']
        else:
            row_data_dict[u'隶属关系'] = u"暂缺"
        row_data_dict[u'现建筑面积'] = item[u'现建筑面积']
        final_data.append(row_data_dict)
    return result_data

def get_museum_list(request):
    province = request.GET.get("province", "全部")
    type1 = request.GET.get("type1", "全部")
    type2 = request.GET.get("type2", "全部")
    type3 = request.GET.get("type3", "全部")

    data = get_list(province,type1, type2, type3)  # type1 场馆级别 type2 单位性质 type3 隶属关系
    result = {"list": data, "total": data.__len__()}

    # result = {"list":[{"ar_name":province_code,"province_name":"北京","article_source":"科普中国","hits":"1000"}]*10,"total":99}

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_museum_information(museum_name):
    file1 = open(sys.path[0] + u'/static/museum_data/2017年全国科技馆调查统计表-192家达标科技馆.json', "r", encoding="utf-8")
    fileJson1 = json.load(file1)
    row_data_dict = {}
    for item in fileJson1:
        if item[u'名称'] == museum_name:
            row_data_dict[u'名称'] = item[u'名称']
            row_data_dict[u'省份'] = item[u'省份']
            row_data_dict[u'场馆级别'] = item[u'场馆级别']
            if u'单位性质' in item:
                row_data_dict[u'单位性质'] = item[u'单位性质']
            else:
                row_data_dict[u'单位性质'] = u"暂缺"
            if u'隶属关系' in item:
                row_data_dict[u'隶属关系'] = item[u'隶属关系']
            else:
                row_data_dict[u'隶属关系'] = u"暂缺"
            row_data_dict[u'现建筑面积'] = item[u'现建筑面积']
            if 'description' in item:
                row_data_dict[u'场馆简介'] = item['description']
                row_data_dict[u'评分'] = item['score']
                row_data_dict[u'评价'] = item['opinions']


    return row_data_dict

def get_museum_info(request):
    museum_name = request.GET.get("museum_name", "中国科学技术馆")

    data = get_museum_information(museum_name)
    result = {"list": data, "total": 1}

    # result = {"list":[{"ar_name":province_code,"province_name":"北京","article_source":"科普中国","hits":"1000"}]*10,"total":99}

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_abstract(museum_name):
    file1 = open(sys.path[0] + u'/static/museum_data/museum_abstract.json', "r", encoding="utf-8")
    fileJson1 = json.load(file1)
    result_data = []
    for item in fileJson1:
        if item[u'名称'] == museum_name:
            if 'abstract' in item:
                abstract = item[u'abstract']
                if abstract == '':
                    row_data_dict = {}
                    row_data_dict['keyword'] = u'暂缺'
                    row_data_dict['id'] = 1
                    result_data.append(row_data_dict)
                    continue
                else:
                    num = 1
                    for key in abstract:
                        row_data_dict = {}
                        row_data_dict['keyword'] = key
                        row_data_dict['id'] = num
                        num += 1
                        result_data.append(row_data_dict)

    return result_data

def get_museum_abstract(request):
    museum_name = request.GET.get("museum_name", "中国科学技术馆")

    data = get_abstract(museum_name)
    #result = {"list": data, "total": 1}

    # result = {"list":[{"ar_name":province_code,"province_name":"北京","article_source":"科普中国","hits":"1000"}]*10,"total":99}

    response = HttpResponse(json.dumps(data, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


