from rest_framework import serializers
from common.models import Project, User


class UserRegistrationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_item = User.objects.create(**validated_data)
        user_item.set_password(password)
        user_item.save()
        return user_item

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

    owner = UserSerializer()

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






