# Generated by Django 3.1.7 on 2021-07-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentToDataLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DataLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_file', models.FileField(upload_to='data_library')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('introduction', models.TextField(max_length=20000, null=True)),
            ],
        ),
    ]
