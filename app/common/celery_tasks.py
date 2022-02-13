from celery import shared_task
from django.core.mail import send_mail
import time


@shared_task
def create_task(task_type):
    send_mail(
        'Subject here',
        'This message was send by celery worker. ',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return True
