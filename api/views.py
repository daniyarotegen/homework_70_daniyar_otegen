from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import IssueSerializer, ProjectSerializer
from tracker.models import Issue, Project


class IssueListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Issue.objects.all()
        serializer = IssueSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.all()
        serializer = ProjectSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IssueDetailView(APIView):

    def get_object(self, pk):
        try:
            return Issue.objects.get(pk=pk)
        except Issue.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        issue = self.get_object(pk)
        serializer = IssueSerializer(issue)
        return Response(serializer.data)

class ProjectDetailView(APIView):

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
