from rest_framework.test import APITestCase
from users.models import User


class TestSignup(APITestCase):
    def test_signup_not_body(self):
        """유저 회원가입 필수 데이터 체크 테스트"""

        response = self.client.post("/api/v1/users/signup/")
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(data, dict)
        self.assertIn("detail", data)

        response = self.client.post("/api/v1/users/signup/", {"password": "test"})
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(data, dict)
        self.assertIn("email", data)
        self.assertIn("username", data)

    def test_signup(self):
        """유저 회원가입 성공 테스트"""

        request_data = {
            "email": "test@gmail.com",
            "username": "test",
            "password": "test",
        }
        response = self.client.post("/api/v1/users/signup/", request_data)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertIn("ok", data)


class TestLogin(APITestCase):
    def setUp(self):
        user = User.objects.create(email="test1@gmail.com", username="test")
        user.set_password("qwer1234!")
        user.save()
        self.user = user

    def test_login_not_body(self):
        """유저 로그인 필수 데이터 체크 테스트"""

        response = self.client.post("/api/v1/users/login/")
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(data, dict)
        self.assertIn("email", data)
        self.assertIn("password", data)

    def test_login_wrong_password(self):
        """유저 로그인 패스워드 오류 테스트"""

        request_data = {
            "email": self.user.email,
            "password": "qwer1234",
        }
        response = self.client.post("/api/v1/users/login/", request_data)
        data = response.json()

        self.assertEqual(response.status_code, 401)
        self.assertIsInstance(data, dict)
        self.assertIn("detail", data)

    def test_login(self):
        """유저 로그인 성공 테스트"""

        request_data = {
            "email": self.user.email,
            "password": "qwer1234!",
        }
        response = self.client.post("/api/v1/users/login/", request_data)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertIn("access", data)
        self.assertIn("refresh", data)
