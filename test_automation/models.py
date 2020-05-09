from django.db import models

# Create your models here.
class TestCase(models.Model):
    '''
    name : 测试案例名
    script : 案例脚本
    script_type : 案例脚本类型 0 settings 1 case
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    script = models.CharField(max_length=256)
    # 0 settings 1 case
    script_type = models.IntegerField()
    test_suite = models.ForeignKey(to="TestSuite", on_delete=False)

class TestSuite(models.Model):
    '''

    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)

class TestJob(models.Model):
    '''
    name : 测试集名称
    suites : 测试套件列表
    rebuild : 重新构建标志　0为无需重构　1为重构
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    suites = models.CharField(max_length=50, blank=False)
    rebuild = models.IntegerField(null=True, blank=True, default=0)