from django.test import TestCase

# Create your tests here.
class UserManagerTest(TestCase):
    def setUp(self):
        pass

    def test_login(self):
        response = self.client.post('http://127.0.0.1:8000/login', data={"username":"admin", "password":"Aa123456"})
        self.assertEqual(response.status_code, 200)
        print(response.json())
        self.assertEqual(response.json().get("code"), 1)