from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def get_results(request):
    if request.method == 'POST':
        data_bytes = request.body
        data_dict = json.loads(data_bytes.decode('utf-8'))
        try:
            match = re.findall(data_dict['regex'], data_dict['text'])
            return JsonResponse({"status": "success", 'results': match})
        except re.error:
            return JsonResponse({"status": "success", 'results': 'Вы ввели неправильное регулярное выражение'})

    else:
        return JsonResponse({"status": "not_success"})


