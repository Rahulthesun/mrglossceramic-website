# Generated by Django 4.2.13 on 2024-06-22 17:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_galleryvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryvideo',
            name='video',
            field=models.FileField(upload_to='gallery/videos/', validators=[django.core.validators.FileExtensionValidator(['mp4'])]),
        ),
    ]
