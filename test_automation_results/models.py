from django.db import models

# Create your models here.
class JobReport(models.Model):
    id = models.AutoField(primary_key=True)
    # 任务名
    job_name = models.CharField(max_length=64, blank=False)
    # 套件名
    suite_name = models.CharField(max_length=64, blank=False)
    # 案例名
    case_name = models.CharField(max_length=64, blank=False)
    # 开始时间
    starttime = models.DateTimeField()
    # 结束时间
    endtime = models.DateTimeField()
    # 执行状态 0 失败 1 成功
    status = models.IntegerField()
    # 日志链接
    url = models.CharField(max_length=512, blank=False)
    # 入库时间
    dt = models.DateTimeField(auto_now=True)