from django.db import models

# Create your models here.
class JobReport(models.Model):
    id = models.AutoField(primary_key=True)
    # 任务
    job_name = models.CharField(max_length=64, blank=False)
    # 套件名
    sutie_name = models.CharField(max_length=64, blank=False)
    # 构建编号
    case_name = models.CharField(max_length=64, blank=False)
    # 构建的日志文件
    url = models.CharField(max_length=512, blank=False)
    # 构建的日期时间
    dt = models.DateTimeField(auto_now=True)
    # 执行状态 0 失败 1 成功
    status = models.IntegerField()