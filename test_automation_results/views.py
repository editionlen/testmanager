from django.shortcuts import render
from shaka.common.response import OK
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def add_job_report(request):
    '''
    {'测试套件': {'baidu_search': {'id': 's1-t1', 'status': 'FAIL', 'starttime': '20200505 13:09:53.829', 'endtime': '20200505 13:09:59.510'}}}
    :param request:
    :return:
    '''
    param = json.loads(request.body)
    job_name = param.get("job_name")
    suites = param.get("suites")
    for suite, cases in suites.items():
        for name, value in cases.items():
            print(job_name, suite, name, value['id'], value['status'], value['starttime'], value['endtime'])
    return OK