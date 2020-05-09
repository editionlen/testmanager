from django.db import models

# Create your models here.
class JobReport(models.Model):
    id = models.AutoField(primary_key=True)
    # 任务
    job = models.ForeignKey(to="test_automation.models.TestJob", on_delete=False)
    # 构建编号
    build_id = models.IntegerField()

    # 任务的测试案例
    case = models.ForeignKey(to="test_automation.models.TestCase", on_delete=False)
    # 构建的日志文件
    build_url = models.CharField(max_length=512, blank=False)
    # 构建的日期时间
    build_datetime = models.DateTimeField(auto_now=True)
    # 执行状态 0 失败 1 成功
    status = models.IntegerField()