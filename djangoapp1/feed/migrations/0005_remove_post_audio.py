# Generated by Django 3.1.5 on 2021-02-07 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_post_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='audio',
        ),
    ]