from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User


class TestHouseholds(APITestCase):
    def setUp(self):
        user = User.objects.create(email="test1@gmail.com", username="test")
        user.set_password("qwer1234!")
        user.save()
        self.user = user

    def test_get_households_not_authorized(self):
        """유저 가계부 내역 비로그인 테스트"""

        response = self.client.get("/api/v1/households/")
        data = response.json()
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", data)

    def test_get_households(self):
        """유저 가계부 내역 성공 테스트"""

        refresh = RefreshToken.for_user(self.user)
        header = {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
        response = self.client.get("/api/v1/households/", **header)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_create_household_not_authorized(self):
        """유저 가계부 내역 작성 비로그인 테스트"""

        response = self.client.post("/api/v1/households/")
        data = response.json()
        self.assertEqual(response.status_code, 401)
        self.assertIn("detail", data)

    def test_create_household_not_body(self):
        """유저 가계부 내역 작성 필수 데이터 체크 테스트"""

        refresh = RefreshToken.for_user(self.user)
        header = {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
        response = self.client.post("/api/v1/households/", **header)
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertIn("amount", data)

    def test_create_household(self):
        """유저 가계부 내역 작성 성공 테스트"""

        request_data = {"amount": 5000, "memo": "편의점"}
        refresh = RefreshToken.for_user(self.user)
        header = {"HTTP_AUTHORIZATION": f"Bearer {refresh.access_token}"}
        response = self.client.post("/api/v1/households/", request_data, **header)
        data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["ok"], True)
