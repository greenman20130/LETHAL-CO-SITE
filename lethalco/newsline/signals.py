from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Message
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Post, User



@receiver(post_save, sender=Message)
def notify_about_new_responce(sender, instance, created, **kwargs):
    if created:
        to_email = User.objects.filter(id=instance.to).values('email')
        to_email = to_email[0]['email']
        html_content = render_to_string(
        'notify/notify_responce_email.html',
        {
            'from': f'{settings.SITE_URL}/posts/profile/{instance.sender_id}',
        }
        )
        to = User.objects.get(id=instance.to)
        print(f'Сообщение отправлено {to}')
        msg = EmailMultiAlternatives(
            subject='Вам отправили отклик',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=(to_email,),
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    else:
        to_email = User.objects.filter(id=instance.to).values('email')
        to_email = to_email[0]['email']
        html_content = render_to_string(
            'notify/notify_accept_email.html',
            {
                'from': f'{settings.SITE_URL}/posts/profile/{sender}',
            }
        )
        to = User.objects.filter(id=instance.to).exists()

        msg = EmailMultiAlternatives(
            subject='Ваш отклик приняли',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=(to_email,),
        )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()