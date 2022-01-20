from django.shortcuts import render
from rest_framework import viewsets
from common.models import Project
from common.serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


