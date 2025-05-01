import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body
    print('body: ', body)
    data = {}
    try:
        data = json.loads(body)
        print('data: ', data)
    except:
        print('failed to parse JSON')
    return JsonResponse(data)