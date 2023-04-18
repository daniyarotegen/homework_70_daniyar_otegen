from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import IssueSerializer
from tracker.models import Issue


class IssueListView(View):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.all()
        serializer = IssueSerializer(objects, many=True)
        return JsonResponse(serializer.data)


class IssueView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.all()
        serializer = IssueSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
