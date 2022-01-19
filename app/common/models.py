from django.db import models
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Project(BaseModel):
    PROJECT_TYPE = (
        ('list', 'Список'),
        ('block', 'Блоки')
    )
    name = models.CharField("Название проекта", max_length=255, blank=True)
    type = models.CharField('Тип блоков', max_length=20, choices=PROJECT_TYPE, default=PROJECT_TYPE[0][0])
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, related_name='project_owner')
    participants = models.ManyToManyField(User, through='Participants')

    def __str__(self):
        return self.name


class Participants(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, related_name='project_participants', on_delete=models.CASCADE)

