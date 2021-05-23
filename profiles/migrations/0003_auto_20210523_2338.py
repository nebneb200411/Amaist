# Generated by Django 3.1.7 on 2021-05-23 14:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_profile_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.ManyToManyField(blank=True, default=None, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, default=None, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
