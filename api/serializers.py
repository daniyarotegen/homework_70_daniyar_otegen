from rest_framework import serializers
from tracker.models import Project


class IssueSerializer(serializers.Serializer):
    summary = serializers.CharField(max_length=200, min_length=5, required=True, allow_blank=True)
    description = serializers.CharField(max_length=3000, required=False, allow_blank=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class ProjectSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date', 'issues')
        read_only_fields = ('start_date', 'end_date', 'issues')