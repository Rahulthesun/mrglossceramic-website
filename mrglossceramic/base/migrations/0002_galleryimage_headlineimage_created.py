# Generated by Django 4.2.13 on 2024-06-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/images/')),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='headlineimage',
            name='created',
            field=models.DateField(auto_now_add=True, default='2000-05-10'),
            preserve_default=False,
        ),
    ]
