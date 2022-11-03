from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.exceptions import NotFound
from .models import Household
from .serializers import HouseholdSerializer
from .permissions import IsOwner


class HouseholdDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        """
        가계부 리스트를 확인합니다.
        GET api/v1/households/
        """

        household = Household.objects.filter(user=request.user, is_active=True)
        serializer = HouseholdSerializer(household, many=True)
        return Response(serializer.data)

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


class HouseholdsView(APIView):

    permission_classes = [IsOwner]

    def get_object(self, pk):
        try:
            household = Household.objects.get(pk=pk)
            self.check_object_permissions(self.request, household)
            return household
        except Household.DoesNotExist:
            raise NotFound

    def patch(self, request, pk):

        """
        가계부의 원하는 내역의 금액과 메모를 수정합니다.
        PATCH api/v1/households/{pk}/
        """

        household = self.get_object(pk)
        serializer = HouseholdSerializer(household, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class HouseholdInactiveView(APIView):

    permission_classes = [IsOwner]

    def get_object(self, pk):
        try:
            household = Household.objects.get(pk=pk)
            self.check_object_permissions(self.request, household)
            return household
        except Household.DoesNotExist:
            raise NotFound

    def post(self, request, pk):

        """
        가계부의 기록을 비활성화 합니다.
        POST api/v1/households/{pk}/inactive
        """

        household = self.get_object(pk)
        household.is_active = False
        household.save()
        return Response({"ok": True})
