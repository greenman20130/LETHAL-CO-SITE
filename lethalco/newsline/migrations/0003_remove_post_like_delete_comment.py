# Generated by Django 5.0.2 on 2024-03-08 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsline', '0002_alter_post_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]