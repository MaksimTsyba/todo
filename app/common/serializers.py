from rest_framework import serializers
from common.models import Project, User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        write_only_fields = ['password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        read_only_fields = ['username']


class ProjectSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    # def validate_name(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError('You need to specify Django in project name')
    #     return value

    def create(self, validated_data: dict) -> Project:
        user = self.context['request'].user
        validated_data['owner'] = user
        return Project.objects.create(**validated_data)

    class Meta:
        model = Project
        fields = ['id', 'name', 'type', 'owner']
        # read_only_fields = ['owner']






