from django.db import models
from common.models import BaseModel


class Section(BaseModel):
    name = models.CharField('Раздел', max_length=255, null=True)
    project = models.ForeignKey('common.Project', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Item(BaseModel):
    STATUS = (
        ('open', 'Открыта'),
        ('close', 'Закрыта')
    )
    title = models.CharField('Название', max_length=255, null=True)
    description = models.TextField('Описание', null=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS, default=STATUS[0][0])
    producer = models.ForeignKey('common.Participants', verbose_name='Постановщик', on_delete=models.SET_NULL,
                                 related_name='item_producer', null=True)
    executor = models.ForeignKey('common.Participants', verbose_name='Исполнитель', on_delete=models.SET_NULL,
                                 related_name='item_executor', null=True)

    def __str__(self):
        return self.title
