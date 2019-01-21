import json
from django.http import HttpResponse
import urllib
import time
import hashlib

def get_online_user_num(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/sciwisdom/getuseronline&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/sciwisdom/getuseronline?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]["num"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_male_user_num(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/dataUser&timestamp="+timestamp+"&type=5&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/dataUser?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn+"&type=5"

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]["man"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_map_nums(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/map&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/map?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    map_num = []

    for d in result["data"]:
        map_num.append({"name":d["area_name"], "value":d["value"]})
    
    response = HttpResponse(json.dumps(map_num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_active_areas(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/areaActive&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/areaActive?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_news(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/news&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/news?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_hotWorld(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/hotWorld&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/hotWorld?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_member_num(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/orgUser&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/orgUser?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_org_num(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/orgEnter&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/orgEnter?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    result = str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8")

    num = json.loads(result)
    data=num["data"]
    XH_map=data["XH_map"]
    KX_map = data["KX_map"]
    for tem in KX_map:
        tem["value"]=tem["num"]
        tem.pop(num)
    for tem in XH_map:
        tem["value"]=tem["num"]
        tem.pop(num)

    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_org_news(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/orgDynamics&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/orgDynamics?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_dynamic(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/dynamics&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/dynamics?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_collect(request):

    timestamp = str(time.time()).split(".")[0]
   
    str1 = "appid=kejie_sciwisdom&path=/Sciwisdom/collect&timestamp="+timestamp+"&secretkey=22306802-02ad-4342-a2ab-2141231d7349"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://openapi.scimall.org.cn/Sciwisdom/collect?appid=kejie_sciwisdom&timestamp="+timestamp+"&sn="+sn

    #print(str(urllib.request.urlopen(url1, timeout=10).read(),encoding="utf-8"))
    
    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))

    num = result["data"]
    
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response




