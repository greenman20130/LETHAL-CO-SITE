from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from .models import Message
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .tasks import send_notifications_responce



@receiver(m2m_changed, sender=Message)
def notify_about_new_responce(sender, instance, **kwargs):
     
    send_notifications_responce.delay(instance.sender, instance.to)

    #elif kwargs['action'] == 