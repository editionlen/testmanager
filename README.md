pip install django==2.0

用户模块（user_manage）
# python manage.py startapp user_manage
python manage.py startapp user_manage
设置时区和语言
Django默认使用美国时间和英语，在项目的settings文件中，如下所示：
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
把它改为亚洲/上海时间和中文
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False
创建用户表
python manage.py makemigrations
python manage.py migrate
创建超级用户
python manage.py createsuperuser
admin
admin@qq.com
Aa123456
Aa123456
登录 POST /login
user_manage.login_view
退出 GET /logout
user_manage.logout_view

设计restful API格式
pip install djangorestframework
需要用什么数据格式就添加什么数据格式
REST_FRAMEWORK={
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    ),
}

测试案例列表模块 
python manage.py startapp test_automation