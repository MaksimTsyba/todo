from django.shortcuts import render
from rest_framework import viewsets
from common.models import Project, User
from common.serializers import ProjectSerializer, UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema, swagger_serializer_method
from common.celery_tasks import create_task
from django.http import JsonResponse
from django.core.mail import send_mail
from drf_yasg import openapi


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return Project.objects.filter(owner=self.request.user).all()
        else:
            return Response(status=HTTP_404_NOT_FOUND)


@swagger_auto_schema(method='post', request_body=UserRegistrationSerializer)
@api_view(['POST'])
def user_registration(request):
    """ User registration"""
    user = UserRegistrationSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response({'code': 200})
    else:
        return Response(user.errors)


def start_task(request):
    task = create_task.delay(int(1))
    return JsonResponse({"task_id": task.id}, status=202)

