import json
from django.shortcuts import HttpResponse

def response(code=1, msg='success', total=0, page=0, data=None):
    if data:
        content = json.dumps(dict(code=code, msg=msg, data=data, total=total, page=page))
    else:
        content = json.dumps(dict(code=code, msg=msg, data=[], total=0, page=0))
    return HttpResponse(content)

def ok(total=1,page=1, data=None):
    return response(total=total,page=page, data=data)

def fail(msg='request failed'):
    return response(msg=msg, code=0)

OK = ok()
Fail = fail()