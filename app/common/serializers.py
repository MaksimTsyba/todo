from rest_framework import serializers
from common.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['name', 'type']





