# Generated by Django 5.0.2 on 2024-03-10 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0004_rename_username_authcode_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authcode',
            name='user',
        ),
    ]
