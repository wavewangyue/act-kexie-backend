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

    print(urllib.request.urlopen(url1, timeout=10).read())
    
    #result1 = json.loads(urllib.request.urlopen(url1, timeout=10).read())
    #result2 = json.loads(urllib.request.urlopen(url2, timeout=10).read())

    #num = result1["data"]["num"] + result2["data"]["num"]
    num=1
    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_sciencers(request):

    province_code = request.GET.get("province_code", None)
    ch_id = request.GET.get("ch_id", None)

    timestamp = str(time.time()).split(".")[0]

    print(timestamp)

    #str1 = "appid=kepu_sciwisdom&ch_id="+ch_id+"&page=1&path=/Articlecount/getSciencerCount&province_code="+province_code+"&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"+"&size=30"
    str1 = "appid=kepu_sciwisdom&path=/Articlecount/getSciencerCount&timestamp="+timestamp+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"
    print(str1)
    sn = hashlib.md5(str1.encode("utf-8")).hexdigest()
    sn = hashlib.md5(sn.encode("utf-8")).hexdigest()
    url = "https://open-api.kepuchina.cn/Articlecount/getSciencerCount?appid=kepu_sciwisdom&timestamp="+timestamp+"&province_code="+province_code+"&ch_id="+ch_id+"&page=1&size=30"+"&sn="+sn+"&secretkey=54f0f716-ae44-4538-b309-d09a96fbad2f"
    print(url)

    result = json.loads(urllib.request.urlopen(url, timeout=10).read())

    num = result

    response = HttpResponse(json.dumps(num, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response