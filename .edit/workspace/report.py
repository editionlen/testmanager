'''
parse output to result and report result to server
'''
import sys
import re
import requests
import json
def parse(filename):
    # output = "D:/project/shaka/.edit/workspace/test/"
    # output_xml = os.path.join(output, "output.xml")
    with open(filename, encoding='utf8') as f:
        lines = f.readlines()
    suites = {}
    suite = ''
    test = ''
    for line in lines:
        if '<suite' in line and 'name' in line:
            suite = re.findall('name="(.+?)"', line)[0]
            suites[suite] = {}
        if '<test' in line and 'name' in line and 'id' in line:
            test = re.findall('name="(.+?)"', line)[0]
            html_id = re.findall('id="(.+?)"', line)[0]
            suites[suite][test] = {"id":html_id}
        if '<status' in line and 'starttime' in line and 'endtime':
            status = re.findall('status="(.+?)"', line)[0]
            suites[suite][test]['status'] = status
            starttime = re.findall('starttime="(.+?)"', line)[0]
            suites[suite][test]['starttime'] = starttime
            endtime = re.findall('endtime="(.+?)"', line)[0]
            suites[suite][test]['endtime'] = endtime
    print(suites)
    return suites

def upload_log(url, job_name):
    files = {'files':open('log.html','rb')}
    response = requests.post(url=url + "?job_name={}".format(job_name), files=files)
    print(response.status_code)

def report(url, name, suites):
    data = {"job_name":name, "suites":suites}
    response = requests.post(url + 'add_job_report', data=json.dumps(data))
    print(response)
    # 上传文件接口
    upload_log(url + 'upload_log', name)


def main():
    name = sys.argv[1]
    url = sys.argv[2]
    suites = parse("output.xml")
    report(url, name, suites)

if __name__ == '__main__':
    main()
