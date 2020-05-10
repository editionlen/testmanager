"""shaka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from user_manage.views import login_view, logout_view, UserViewSet, GroupViewSet
from test_automation.views import import_case_by_local, load_test_suite_list, create_test_job, add_test_case, load_test_case_list, build_test_job, load_test_job_list
from test_automation_results.views import add_job_report

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^login$', login_view),
    url(r'^logout$', logout_view),
    url(r'^import_case_by_local$', import_case_by_local),
    url(r'^load_test_suite_list$', load_test_suite_list),
    url(r'^load_test_case_list$', load_test_case_list),
    url(r'^load_test_job_list$', load_test_job_list),
    url(r'^create_test_job$', create_test_job),
    url(r'^add_test_case$', add_test_case),
    url(r'^build_test_job$', build_test_job),
    url(r'^add_job_report$', add_job_report),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
