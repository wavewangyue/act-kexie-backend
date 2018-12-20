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






