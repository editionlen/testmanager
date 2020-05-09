from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json
import traceback
# Create your views here.
@csrf_exempt
def login_view(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse(json.dumps({"code":1, "msg":"success"}), content_type="application/json")
        return HttpResponse(json.dumps({"code": 0, "msg": "user or password error"}), content_type="application/json")
    except Exception as e:
        traceback.print_exc()
        return HttpResponse(json.dumps({"code": 0, "msg": "interface error"}), content_type="application/json")

def logout_view(request):
    logout(request)
    return HttpResponse(json.dumps({"code": 1, "msg": "success"}), content_type="application/json")

from django.http import JsonResponse
from rest_framework.views import APIView

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from user_manage.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer