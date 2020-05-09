import requests
import json
class TestShaka:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.url = "http://127.0.0.1:8000/"
        self.session = requests.session()

    def login(self):
        res = self.session.post(self.url + 'login', data={"username":"admin", "password":"Aa123456"})
        print(res.text)

    def logout(self):
        res = self.session.get(self.url + 'logout')
        print(res)

    def add_test_case(self):
        data = {"name": "baidu_search",
                "script": "    Open Browser    http://www.baidu.com    chrome\n    Input Text    id=kw    robotframework学习\n    Press Key    id=kw    \\13\n    sleep    6\n    close Browser",
                "script_type": 1,
                "test_suite_id": 1}
        res = self.session.post(self.url + 'add_test_case', data=json.dumps(data, ensure_ascii=True))
        print(res.text)

    def create_test_job(self):
        data = {"name":"test", "suites":"1,2,3"}
        res = self.session.post(self.url + 'create_test_job', data=json.dumps(data, ensure_ascii=True))
        print(res.text)

    def build_test_job(self):
        data = {"id":1}
        res = self.session.post(self.url + 'build_test_job', data=json.dumps(data, ensure_ascii=True))
        print(res.text)

    def run(self):
        self.login()
        # self.add_test_case()
        # self.create_test_job()
        self.build_test_job()
        self.logout()

if __name__ == '__main__':
    test_shaka = TestShaka("admin", "Aa123456")
    test_shaka.run()
