import json
from django.http import HttpResponse

def search_xuehui(request):
    name = request.GET.get('name', None)
    if name:
        result = "success"
    else:
        result = "wrong param"

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    response["Access-Control-Allow-Origin"] = "*"
    return response