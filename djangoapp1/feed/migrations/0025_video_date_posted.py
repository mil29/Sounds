# Generated by Django 3.1.5 on 2021-04-26 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0024_video_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
