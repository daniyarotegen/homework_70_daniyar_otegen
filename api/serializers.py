from rest_framework import serializers
from tracker.models import Project


class IssueSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    summary = serializers.CharField(max_length=200, min_length=4, required=True, allow_blank=True)
    description = serializers.CharField(max_length=3000, required=False, allow_blank=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        instance.summary = validated_data.get('summary', instance.summary)
        instance.description = validated_data.get('description', instance.description)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('pk', 'name', 'description', 'start_date', 'end_date', 'issues')
        read_only_fields = ('start_date', 'end_date', 'issues')