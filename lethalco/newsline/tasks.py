
import datetime
from .models import Post, User
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


# def send_notifications_accept(sender, to):
#     html_content = render_to_string(
#         'notify/notify_accept_email.html',
#         {
#             'from': f'{settings.SITE_URL}/posts/profile/{sender}',
#         }
#     )
#     to = User.objects.filter(id=to).exists()

#     msg = EmailMultiAlternatives(
#         subject='Ваш отклик приняли',
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=to['email'],
#     )

#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()


def send_notifications_responce(sender, to):
    html_content = render_to_string(
        'notify/notify_responce_email.html',
        {
            'from': f'{settings.SITE_URL}/posts/profile/{sender}',
        }
    )
    to = User.objects.filter(id=to).get('email')
    print('Сообщение отправлено {to}')
    msg = EmailMultiAlternatives(
        subject='Вам отправили отклик',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()