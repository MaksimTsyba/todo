from django.db.models.signals import post_save, pre_save
from django.core.mail import send_mail
from django.dispatch import receiver
from common.models import Project, User


@receiver(post_save, sender=User)
def set_password_for_user(*args, **kwargs):
    """ Convert password and set this one to user """
    if kwargs['created'] is True:
        password = kwargs['instance'].password
        kwargs['instance'].set_password(password)
        kwargs['instance'].save()


@receiver(post_save, sender=Project)
def project_created(*args, **kwargs):
    print('post_save')
    print(kwargs)
    print(kwargs['instance'].id)
    print(kwargs['instance'].name)
    # send_mail(
    #     'Subject here',
    #     'This message was send from signal. ',
    #     'from@example.com',
    #     ['to@example.com'],
    #     fail_silently=False,
    # )

