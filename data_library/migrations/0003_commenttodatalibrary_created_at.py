# Generated by Django 3.1.7 on 2021-07-08 12:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data_library', '0002_auto_20210704_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='commenttodatalibrary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
