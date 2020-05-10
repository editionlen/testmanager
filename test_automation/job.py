import os
import django
# 在environ字典里设置默认Django环境，'xxxx.settings'指Django项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shaka.settings')
django.setup()

import jenkins
from shaka.settings import JenkinsConfig
from test_automation.models import TestJob, TestCase

def build(test_job_id):
    test_job = TestJob.objects.get(id=test_job_id)
    name = test_job.name
    suites = test_job.suites
    rebuild = test_job.rebuild
    t = Job(name=name, suites=suites, rebuild=rebuild)
    if rebuild:
        t.create()
        test_job.rebuild = 0
        test_job.save()
    t.build()

def suites_to_robot(suites, job_name):
    path = os.path.join(JenkinsConfig.workspace, job_name)
    if os.path.isdir(path):
        pass
    else:
        os.makedirs(path)
    obj = TestCase.objects.raw("select t1.id as id, t1.name as filename, t2.name as case_name, t2.script_type as script_type, t2.script as script  from test_automation_testsuite t1 inner join test_automation_testcase t2 ON t1.id = t2.test_suite_id where t1.id in ({}) order by t1.id, t2.script_type".format(suites))
    settings = {}
    cases = {}
    files = []
    for row in obj:
        file_path = os.path.join(path, row.filename)
        if file_path not in files:
            files.append(file_path)
            settings[file_path] = []
            cases[file_path] = []
        if row.script_type == 0:
            settings[file_path].append(row.script)
        elif row.script_type == 1:
            cases[file_path].append([row.case_name, row.script])
    file = files[0]
    with open(file, 'w+', encoding='utf8') as f:
        f.write('*** Settings ***\n')
        f.write(''.join(settings.get(file)))
        f.write('\n*** Test Cases ***\n')
        for case in cases.get(file):
            f.write(case[0])
            f.write('\n{}'.format(case[1]))
    url_rf_path = JenkinsConfig.download_url + job_name + '/' + file
    rf_file = file
    return url_rf_path, rf_file

# def build(name, suites, rebuild, url_rf_path, rf_file):
#     print(name)
#     t = Job(name, suites, rebuild, url_rf_path, rf_file)
#     t.create()
#     t.build()

class Job:
    def __init__(self,
                 name=None,
                 suites='',
                 rebuild=0):
        self.server = jenkins.Jenkins(JenkinsConfig.url, JenkinsConfig.user, JenkinsConfig.password)
        self.name = name
        self.suites = suites
        self.rebuild = rebuild

    def create(self):
        url_rf_path, rf_file = suites_to_robot(self.suites, self.name)
        configure = JenkinsConfig.template.format(
            url_rf_path=url_rf_path,
            rf_file=rf_file,
            get_report_url=JenkinsConfig.download_url + 'report.py',
            add_job_report=JenkinsConfig.upload_url
        )
        if self.server.job_exists(self.name):
            if self.rebuild:
                self.server.reconfig_job(self.name, configure)
        else:
            self.server.create_job(self.name, configure)

    def build(self):
        self.server.build_job(self.name, parameters={"id":1})

if __name__ == '__main__':
    suites_to_robot('1', 'test')