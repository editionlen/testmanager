import os
import json
from shaka.settings import EDIT_HOME
from shaka.common.response import ok, OK
from django.views.decorators.csrf import csrf_exempt
from test_automation.script_to_sql import script_to_sql
from test_automation.models import *
from test_automation.serializers import *
from django.core import serializers
from test_automation import job
# Create your views here.
def get_edit_test_job(request):
    pass

@csrf_exempt
def import_case_by_local(request):
    '''
    导入robotframework脚本，并存入数据库
    :param request:
    :return:
    '''
    file = request.FILES.get('files')
    # 文件路径
    path = os.path.join(EDIT_HOME, "upload", file.name)
    with open(path, 'wb') as f:
        for i in file.chunks():
            f.write(i)
    with open(path, encoding='utf8') as f:
        lines = f.readlines()
    test_suite_obj = TestSuite(name=file.name)
    test_suite_obj.save()
    settings, cases = script_to_sql(lines)
    t1 = TestCase(name='settings', script='\n'.join(settings), script_type=0, test_suite=test_suite_obj)
    t1.save()
    for k,v in cases.items():
        t = TestCase(name=k, script=v, script_type=1, test_suite=test_suite_obj)
        t.save()
    return OK

@csrf_exempt
def load_test_suite_list(request):
    objects = TestSuite.objects.all()
    serializer = TestSuiteSerializer(objects, many=True)
    data = serializer.data
    print(data)
    return ok(data=data)

@csrf_exempt
def load_test_case_list(request):
    objects = TestCase.objects.all()
    serializer = TestCaseSerializer(objects, many=True)
    data = serializer.data
    print(data)
    return ok(data=data)

@csrf_exempt
def add_test_case(request):
    data = json.loads(request.body)
    data["test_suite"] = data.pop("test_suite_id")
    t = TestCaseSerializer(data=data)
    t.is_valid()
    t.save()
    return OK

@csrf_exempt
def delete_test_case(request):
    data = json.loads(request.body)
    test_case_id = data.pop("test_case_id")
    t = TestCase.objects.get(id=test_case_id)
    t.delete()
    return OK

@csrf_exempt
def delete_test_suite(request):
    data = json.loads(request.body)
    test_suite_id = data.pop("test_suite_id")
    t = TestCase.objects.get(id=test_suite_id)
    t.delete()
    return OK

@csrf_exempt
def create_test_job(request):
    data = json.loads(request.body)
    t = TestJobSerializer(data=data)
    t.is_valid()
    t.save()
    return OK

def load_test_job_list(request):
    objects = TestJob.objects.all()
    data = json.loads(serializers.serialize("json", objects))
    print(data)
    return ok(data=data)

@csrf_exempt
def build_test_job(request):
    param = json.loads(request.body)
    test_job_id = param['id']
    job.build(test_job_id)
    return OK

@csrf_exempt
def delete_test_job(request):
    param = json.loads(request.body)
    test_job_id = param['id']
    job.delete_job(test_job_id)
    return OK