import json
from django.http import HttpResponse
import urllib
import time
import hashlib

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

    num = result1["data"]["num"] + result2["data"]["num"]
    #num=1
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response



def get_per(request):

    province_code = request.GET.get("province_code", "110000000000")
    ch_id = request.GET.get("ch_id", "AT201605110953441010")

    timestamp = str(time.time()).split(".")[0]

    str1 = "appid=kepu_sciwisdom&ch_id="+ch_id+"&page=1&path=/Articlecount/getSciencerCount&province_code="+province_code+"&size=20&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://open-api.kepuchina.cn/Articlecount/getSciencerCount?appid=kepu_sciwisdom&timestamp="+timestamp+"&province_code="+province_code+"&ch_id="+ch_id+"&page=1&size=20"+"&sn="+sn

    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))
    
    result = result["data"]["list"]

    result = [{"sciencer_name":province_code,"province_name":ch_id,"experience":ch_id}]*20

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response





def get_org(request):

    province_code = request.GET.get("province_code", "110000000000")
    ch_id = request.GET.get("ch_id", "AT201605110953441010")

    timestamp = str(time.time()).split(".")[0]

    str1 = "appid=kepu_sciwisdom&ch_id="+ch_id+"&page=1&path=/Articlecount/getSourceCount&province_code="+province_code+"&size=20&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"  
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://open-api.kepuchina.cn/Articlecount/getSourceCount?appid=kepu_sciwisdom&timestamp="+timestamp+"&province_code="+province_code+"&ch_id="+ch_id+"&page=1&size=20"+"&sn="+sn

    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))
    
    result = result["data"]["list"]

    result = [{"article_source":"科普中国","province_name":"北京","num":"1100"}]*8

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response



def get_art(request):

    province_code = request.GET.get("province_code", "110000000000")
    ch_id = request.GET.get("ch_id", "AT201605110953441010")

    timestamp = str(time.time()).split(".")[0]

    str1 = "appid=kepu_sciwisdom&ch_id="+ch_id+"&page=1&path=/Articlecount/getArticleCount&province_code="+province_code+"&size=20&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"  
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://open-api.kepuchina.cn/Articlecount/getArticleCount?appid=kepu_sciwisdom&timestamp="+timestamp+"&province_code="+province_code+"&ch_id="+ch_id+"&page=1&size=20"+"&sn="+sn

    result = json.loads(str(urllib.request.urlopen(url, timeout=10).read(),encoding="utf-8"))
    
    result = result["data"]["list"]

    result = [{"ar_name":province_code,"province_name":"北京","article_source":"科普中国","hits":"1000"}]*4

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


