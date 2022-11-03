from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from .serializers import HouseholdSerializer


class HouseholdDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        """
        사용한 돈의 금액과 관련된 메모를 남깁니다.
        POST api/v1/households/
        """

        serializer = HouseholdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"ok": True}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
