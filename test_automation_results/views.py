from django.shortcuts import render
from shaka.common.response import OK
from django.views.decorators.csrf import csrf_exempt
from test_automation_results.serializers import JobReportSerializer
import json
import time
from datetime import datetime
import os
from shaka.settings import EDIT_HOME
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
    for suite_name, cases in suites.items():
        for case_name, value in cases.items():
            url = '/static/workspace/{}/log.html#'.format(job_name) + value['id']
            starttime = time.mktime(time.strptime(value['starttime'], '%Y%m%d %H:%M:%S.%f'))
            endtime = time.mktime(time.strptime(value['endtime'], '%Y%m%d %H:%M:%S.%f'))
            if value['status'] == 'PASS':
                status = 1
            else:
                status = 0
            record = dict(job_name=job_name,
                          suite_name=suite_name,
                          case_name=case_name,
                          starttime=datetime.fromtimestamp(starttime),
                          endtime=datetime.fromtimestamp(endtime),
                          status=status,
                          url=url
                          )
            job_report = JobReportSerializer(data=record)
            job_report.is_valid()
            job_report.save()
    return OK

@csrf_exempt
def upload_log(request):
    file = request.FILES.get('files')
    job_name = request.GET['job_name']
    # 文件路径
    path = os.path.join(EDIT_HOME, "workspace", job_name, file.name)
    with open(path, 'wb') as f:
        for i in file.chunks():
            f.write(i)
    return OK