# Generated by Django 3.2.20 on 2023-09-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
