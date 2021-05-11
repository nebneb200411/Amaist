# Generated by Django 3.1.7 on 2021-05-11 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_remove_user_articles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_to', to=settings.AUTH_USER_MODEL)),
                ('follow_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
