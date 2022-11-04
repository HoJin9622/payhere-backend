from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.exceptions import ParseError
from .serializers import UserSerializer


class SignupView(APIView):
    def post(self, request):
        """
        유저 회원가입
        POST api/v1/users/signup/
        """
        password = request.data.get("password")
        if not password:
            raise ParseError("패스워드는 필수입니다.")

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response({"ok": True})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
